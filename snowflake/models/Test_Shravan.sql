{{
  config({    
    "materialized": "table"
  })
}}

WITH STUDENTS AS (

  SELECT * 
  
  FROM {{ source('SNOWFLAKE_LEARNING_DB.PUBLIC', 'STUDENTS') }}

),

Aggregate_1 AS (

  SELECT 
    STUDENT_ID AS STUDENT_ID,
    CONCAT(FIRST_NAME, ' ', LAST_NAME) AS Full_name,
    DATE_OF_BIRTH AS DATE_OF_BIRTH,
    GENDER AS GENDER,
    EMAIL AS EMAIL,
    PHONE AS PHONE,
    ENROLL_DATE AS ENROLL_DATE,
    GPA AS GPA
  
  FROM STUDENTS AS in0

),

student_information AS (

  SELECT 
    STUDENT_ID AS STUDENT_ID,
    FULL_NAME AS FULL_NAME,
    DATE_OF_BIRTH AS DATE_OF_BIRTH,
    GENDER AS GENDER,
    EMAIL AS EMAIL,
    GPA AS GPA
  
  FROM Aggregate_1 AS in0

),

student_gpa_rankings AS (

  SELECT 
    *,
    DENSE_RANK() OVER (PARTITION BY GENDER ORDER BY GPA DESC) AS rank
  
  FROM student_information AS in0

),

gender_gpa_statistics AS (

  SELECT 
    GENDER AS gender,
    AVG(GPA) AS Avg_GPA,
    MAX(GPA) AS max_gpa,
    MIN(GPA) AS min_gpa
  
  FROM student_gpa_rankings AS in0
  
  GROUP BY GENDER

)

SELECT *

FROM gender_gpa_statistics
