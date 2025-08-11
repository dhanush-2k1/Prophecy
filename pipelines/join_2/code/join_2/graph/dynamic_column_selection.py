from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from join_2.config.ConfigStore import *
from join_2.functions import *

def dynamic_column_selection(spark: SparkSession, Employee_join: DataFrame) -> DataFrame:
    from typing import Optional, List, Dict
    from dataclasses import dataclass, field
    from abc import ABC
    
    from pyspark.sql.column import Column
    from pyspark.sql.functions import col
    from dataclasses import dataclass
    from typing import Optional, List, Dict
    from pyspark.sql.column import Column as sparkColumn


    @dataclass(frozen = True)
    class SColumn:
        expression: Optional[Column] = None

        @staticmethod
        def getSColumn(column: str):
            return SColumn(col(column))

        def column(self) -> sparkColumn:
            return self.expression

        def columnName(self) -> str:
            return self.expression._jc.toString()


    @dataclass(frozen = True)
    class SColumnExpression:
        target: str
        expression: SColumn
        description: str
        _row_id: Optional[str] = None

        @staticmethod
        def remove_backticks(s):
            if s.startswith("`") and s.endswith("`"):
                return s[1:- 1]
            else:
                return s

        @staticmethod
        def getColumnExpression(column: str):
            return SColumnExpression(column, SColumn.getSColumn(col(column)), "")

        @staticmethod
        def getColumnsFromColumnExpressionList(columnExpressions: list):
            columnList = []

            for expression in columnExpressions:
                columnList.append(expression.expression)

            return columnList

        def column(self) -> Column:

            if (self.expression.columnName() == SColumnExpression.remove_backticks(self.target)):
                return self.expression.expression

            return self.expression.expression.alias(self.target)


    @dataclass(frozen = True)
    class DynamicSelectProperties():
        selectUsing: str = "SELECT_FIELD_TYPES"
        # DATA TYPES
        boolTypeChecked: bool = False
        strTypeChecked: bool = False
        intTypeChecked: bool = False
        shortTypeChecked: bool = False
        byteTypeChecked: bool = False
        longTypeChecked: bool = False
        floatTypeChecked: bool = False
        doubleTypeChecked: bool = False
        decimalTypeChecked: bool = False
        binaryTypeChecked: bool = False
        dateTypeChecked: bool = False
        timestampTypeChecked: bool = False
        structTypeChecked: bool = False
        # custom expression
        customExpression: Optional[str] = None

    props = DynamicSelectProperties(  #skiptraversal
        selectUsing = "SELECT_FIELD_TYPES", 
        boolTypeChecked = False, 
        strTypeChecked = True, 
        intTypeChecked = True, 
        shortTypeChecked = False, 
        byteTypeChecked = False, 
        longTypeChecked = False, 
        floatTypeChecked = False, 
        doubleTypeChecked = False, 
        decimalTypeChecked = False, 
        binaryTypeChecked = False, 
        dateTypeChecked = False, 
        timestampTypeChecked = False, 
        structTypeChecked = False, 
        customExpression = None
    )
    in0 = Employee_join

    if props.selectUsing == "SELECT_FIELD_TYPES":
        desired_types = []
        type_mapping = {
            'strTypeChecked': "string",
            'intTypeChecked': "int",
            'boolTypeChecked': "boolean",
            'shortTypeChecked': "short",
            'byteTypeChecked': "byte",
            'longTypeChecked': "long",
            'floatTypeChecked': "float",
            'doubleTypeChecked': "double",
            'decimalTypeChecked': "decimal",
            'binaryTypeChecked': "binary",
            'dateTypeChecked': "date",
            'timestampTypeChecked': "timestamp",
            'structTypeChecked': "struct"
        }

        for prop, type_name in type_mapping.items():
            if getattr(props, prop):
                desired_types.append(type_name)

        from prophecy.libs.utils import filter_columns_by_type

        return filter_columns_by_type(spark, in0, ",".join(desired_types))
    else:
        from prophecy.libs.utils import filter_columns_by_expr

        return filter_columns_by_expr(spark, in0, props.customExpression)
