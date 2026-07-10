# dbo.vwDW_SFSCube_Age_KidBreakout

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_Age_KidBreakout"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_Age_KidBreakout]
AS
SELECT  CAST(10 AS DECIMAL(4, 1)) AS ageKey,
        CAST(0 AS DECIMAL(4, 1)) AS minAge,
        CAST(0.9 AS DECIMAL(4, 1)) AS maxAge,
        CAST(10 AS SMALLINT) AS relSeq,
        CAST('0 Years' AS VARCHAR(10)) AS Descr
UNION ALL
SELECT  20 AS ageKey,
        1 AS minAge,
        3.9 AS maxAge,
        20 AS relSeq,
        '1-3 Yrs' AS Descr
UNION ALL
SELECT  30 AS ageKey,
        4 AS minAge,
        6.9 AS maxAge,
        30 AS relSeq,
        '4-6 Yrs' AS Descr
UNION ALL
SELECT  40 AS ageKey,
        7 AS minAge,
        9.9 AS maxAge,
        40 AS relSeq,
        '7-9 Yrs' AS Descr
UNION ALL
SELECT  50 AS ageKey,
        10 AS minAge,
        12.9 AS maxAge,
        50 AS relSeq,
        '10-12 Yrs' AS Descr
UNION ALL
SELECT  60 AS ageKey,
        13 AS minAge,
        19.9 AS maxAge,
        60 AS relSeq,
        '13-19 Yrs' AS Descr
UNION ALL
SELECT  70 AS ageKey,
        20 AS minAge,
        32767 AS maxAge,
        70 AS relSeq,
        '20 +' AS Descr
UNION ALL
SELECT  -1 AS ageKey,
        -32767 AS minAge,
        -0.1 AS maxAge,
        80 AS relSeq,
        'Unknown' AS Descr
```

