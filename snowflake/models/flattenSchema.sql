{{
  config({    
    "materialized": "incremental",
    "incremental_strategy": "append"
  })
}}

WITH STUDENTS AS (

  SELECT * 
  
  FROM {{ source('SNOWFLAKE_LEARNING_DB.PUBLIC', 'STUDENTS') }}

),

Subgraph_1 AS (

  WITH student_performance_summary AS (
  
    SELECT 
      STUDENT_ID AS STUDENT_ID,
      CONCAT(FIRST_NAME, ' ', LAST_NAME) AS full_name,
      DATE_OF_BIRTH AS DATE_OF_BIRTH,
      GENDER AS GENDER,
      EMAIL AS EMAIL,
      PHONE AS PHONE,
      ENROLL_DATE AS ENROLL_DATE,
      GPA AS GPA,
      CASE
        WHEN GPA >= 3.9 and GPA <= 4.0
          THEN 'Excellent'
        WHEN gpa >= 3.75 and gpa <= 3.89
          THEN 'very Good'
        WHEN gpa >= 3.5 and gpa <= 3.74
          THEN 'Good'
        WHEN gpa >= 3.0 and gpa <= 3.49
          THEN 'Above Average'
        WHEN gpa >= 2.5 and gpa <= 2.99
          THEN 'Average'
        WHEN gpa >= 2.0 and gpa <= 2.49
          THEN 'Below Average'
        WHEN gpa <= 1.99
          THEN 'Fail'
      END AS Performance
    
    FROM STUDENTS AS in0
  
  ),
  
  excellent_performance_records AS (
  
    SELECT * 
    
    FROM student_performance_summary AS in0
    
    WHERE PERFORMANCE = 'Excellent'
  
  )
  
  SELECT * 
  
  FROM excellent_performance_records

)

SELECT *

FROM Subgraph_1
