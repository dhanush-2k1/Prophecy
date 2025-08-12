{{
  config({    
    "materialized": "table"
  })
}}

WITH STUDENTS AS (

  SELECT * 
  
  FROM {{ source('SNOWFLAKE_LEARNING_DB.PUBLIC', 'STUDENTS') }}

)

SELECT *

FROM STUDENTS
