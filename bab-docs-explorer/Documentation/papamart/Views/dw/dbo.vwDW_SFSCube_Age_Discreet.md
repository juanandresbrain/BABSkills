# dbo.vwDW_SFSCube_Age_Discreet

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_Age_Discreet"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_Age_Discreet]
AS
SELECT     CAST(10 AS DECIMAL(4, 1)) AS ageKey, CAST(0 AS DECIMAL(4, 1)) AS minAge, CAST(0.9 AS DECIMAL(4, 1)) AS maxAge, CAST(10 AS SMALLINT) AS relSeq, 
                      CAST('0' AS VARCHAR(10)) AS Descr
UNION ALL
SELECT     21 AS ageKey, 1 AS minAge, 1.9 AS maxAge, 20 AS relSeq, '1 Yr' AS Descr
UNION ALL
SELECT     22 AS ageKey, 2 AS minAge, 2.9 AS maxAge, 22 AS relSeq, '2 Yrs' AS Descr
UNION ALL
SELECT     23 AS ageKey, 3 AS minAge, 3.9 AS maxAge, 23 AS relSeq, '3 Yrs' AS Descr
UNION ALL
SELECT     24 AS ageKey, 4 AS minAge, 4.9 AS maxAge, 24 AS relSeq, '4 Yrs' AS Descr
UNION ALL
SELECT     25 AS ageKey, 5 AS minAge, 5.9 AS maxAge, 25 AS relSeq, '5 Yrs' AS Descr
UNION ALL
SELECT     26 AS ageKey, 6 AS minAge, 6.9 AS maxAge, 26 AS relSeq, '6 Yrs' AS Descr
UNION ALL
SELECT     27 AS ageKey, 7 AS minAge, 7.9 AS maxAge, 27 AS relSeq, '7 Yrs' AS Descr
UNION ALL
SELECT     28 AS ageKey, 8 AS minAge, 8.9 AS maxAge, 28 AS relSeq, '8 Yrs' AS Descr
UNION ALL
SELECT     29 AS ageKey, 9 AS minAge, 9.9 AS maxAge, 29 AS relSeq, '9 Yrs' AS Descr
UNION ALL
SELECT     30 AS ageKey, 10 AS minAge, 10.9 AS maxAge, 30 AS relSeq, '10 Yrs' AS Descr
UNION ALL
SELECT     31 AS ageKey, 11 AS minAge, 11.9 AS maxAge, 31 AS relSeq, '11 Yrs' AS Descr
UNION ALL
SELECT     32 AS ageKey, 12 AS minAge, 12.9 AS maxAge, 32 AS relSeq, '12 Yrs' AS Descr
UNION ALL
SELECT     33 AS ageKey, 13 AS minAge, 13.9 AS maxAge, 33 AS relSeq, '13 Yrs' AS Descr
UNION ALL
SELECT     34 AS ageKey, 14 AS minAge, 14.9 AS maxAge, 34 AS relSeq, '14 Yrs' AS Descr
UNION ALL
SELECT     35 AS ageKey, 15 AS minAge, 15.9 AS maxAge, 35 AS relSeq, '15 Yrs' AS Descr
UNION ALL
SELECT     36 AS ageKey, 16 AS minAge, 16.9 AS maxAge, 36 AS relSeq, '16 Yrs' AS Descr
UNION ALL
SELECT     37 AS ageKey, 17 AS minAge, 17.9 AS maxAge, 37 AS relSeq, '17 Yrs' AS Descr
UNION ALL
SELECT     38 AS ageKey, 18 AS minAge, 18.9 AS maxAge, 38 AS relSeq, '18 Yrs' AS Descr
UNION ALL
SELECT     70 AS ageKey, 19 AS minAge, 32767 AS maxAge, 70 AS relSeq, '19 +' AS Descr
UNION ALL
SELECT     - 1 AS ageKey, - 32767 AS minAge, -0.1 AS maxAge, 80 AS relSeq, 'Unknown' AS Descr
```

