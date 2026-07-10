# dbo.vwDW_SFSCube_SinceLastTransaction

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_SinceLastTransaction"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_SinceLastTransaction]
AS
SELECT     CAST(10 AS SMALLINT) AS ageKey, CAST(1 AS SMALLINT) AS minDays, CAST(90 AS SMALLINT) AS maxDays, CAST(10 AS SMALLINT) AS relSeq, 
                      CAST('0-3 Mo' AS VARCHAR(10)) AS Descr
UNION ALL
SELECT     21 AS ageKey, 91 AS minDays, 180 AS maxDays, 20 AS relSeq, '4-6 Mo' AS Descr
UNION ALL
SELECT     22 AS ageKey, 181 AS minDays, 270 AS maxDays, 22 AS relSeq, '7-9 Mo' AS Descr
UNION ALL
SELECT     23 AS ageKey, 271 AS minDays, 365 AS maxDays, 23 AS relSeq, '10-12 Mo' AS Descr
UNION ALL
SELECT     24 AS ageKey, 366 AS minDays, 546 AS maxDays, 24 AS relSeq, '13-18 Mo' AS Descr
UNION ALL
SELECT     25 AS ageKey, 547 AS minDays, 720 AS maxDays, 25 AS relSeq, '19-24 Mo' AS Descr
UNION ALL
SELECT     70 AS ageKey, 721 AS minDays, 32767 AS maxDays, 70 AS relSeq, '2+ Years' AS Descr
UNION ALL
SELECT     90 AS ageKey, - 1 AS minDays, 0 AS maxDays, 5 AS relSeq, 'Never' AS Descr
UNION ALL
SELECT     - 1 AS ageKey, - 32767 AS minDays, - 2 AS maxDays, 80 AS relSeq, 'Unknown' AS Descr
```

