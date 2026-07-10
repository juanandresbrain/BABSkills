# dbo.vwDW_SFSCube_Age_TweenBreakout

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_Age_TweenBreakout"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_Age_TweenBreakout]
AS
SELECT  CAST(10 AS DECIMAL(4, 1)) AS ageKey,
        CAST(0 AS DECIMAL(4, 1)) AS minAge,
        CAST(0.9 AS DECIMAL(4, 1)) AS maxAge,
        CAST(10 AS SMALLINT) AS relSeq,
        CAST('0 Years' AS VARCHAR(10)) AS Descr
UNION ALL
SELECT  20 AS ageKey,
        1 AS minAge,
		2.9 AS maxAge,
        20 AS relSeq,
        '1-2 Yrs' AS Descr
UNION ALL
SELECT  30 AS ageKey,
        3 AS minAge,
        7.9 AS maxAge,
        30 AS relSeq,
        '3-7 Yrs' AS Descr
UNION ALL
SELECT  40 AS ageKey,
        8 AS minAge,
        12.9 AS maxAge,
        40 AS relSeq,
        '8-12 Yrs' AS Descr
UNION ALL
SELECT  50 AS ageKey,
        13 AS minAge,
        19.9 AS maxAge,
        50 AS relSeq,
        '13-19 Yrs' AS Descr
UNION ALL
SELECT  60 AS ageKey,
        20 AS minAge,
        29.9 AS maxAge,
        60 AS relSeq,
        '20-29 Yrs' AS Descr
UNION ALL
SELECT  70 AS ageKey,
        30 AS minAge,
        32767 AS maxAge,
        70 AS relSeq,
        '30 +' AS Descr
UNION ALL
SELECT  -1 AS ageKey,
        -32767 AS minAge,
        -0.1 AS maxAge,
        80 AS relSeq,
        'Unknown' AS Descr
```

