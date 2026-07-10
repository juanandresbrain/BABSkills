# dbo.vwDW_SFSCube_Age_NewAgeBracket2014

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_Age_NewAgeBracket2014"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_Age_NewAgeBracket2014]
AS
SELECT  CAST(1 AS DECIMAL(4, 1)) AS ageKey,
        CAST(0 AS DECIMAL(4, 1)) AS minAge,
        CAST(2.9 AS DECIMAL(4, 1)) AS maxAge,
        CAST(10 AS SMALLINT) AS relSeq,
        CAST('0 - 2' AS VARCHAR(10)) AS Descr
UNION ALL
SELECT  3 AS ageKey,
        3 AS minAge,
		6.4 AS maxAge,
        20 AS relSeq,
        '3 - 6.5' AS Descr
UNION ALL
SELECT  7 AS ageKey,
        6.5 AS minAge,
        9.9 AS maxAge,
        30 AS relSeq,
        '6.5 - 9' AS Descr
UNION ALL
SELECT 10 AS ageKey,
        10 AS minAge,
        12.9 AS maxAge,
        40 AS relSeq,
        '10 - 12' AS Descr
UNION ALL
SELECT  13 AS ageKey,
        13 AS minAge,
        32767 AS maxAge,
        50 AS relSeq,
        '13 +' AS Descr
UNION ALL
SELECT  -1 AS ageKey,
        -32767 AS minAge,
        -0.1 AS maxAge,
        80 AS relSeq,
        'Unknown' AS Descr
```

