# dbo.vwDW_SFSCube_Distance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_Distance"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_Distance]
AS
SELECT     - 1 AS distance_key, CAST('Unknown' AS varchar(50)) AS descr, CAST(- 32767 AS float) AS minDistance
			, CAST(.1 AS float) AS maxDistance, 
                      CAST(999 AS smallint) AS relSeq
union all 
select 10 as distance_key, '0-5 Mi' as descr, .1 as minDistance, 5 as maxDistance, 10 as relSeq
union all 
select 20 as distance_key, '5-10 Mi' as descr, 5 as minDistance, 10 as maxDistance, 20 as relSeq
union all 
select 30 as distance_key, '10-15 Mi' as descr, 10 as minDistance, 15 as maxDistance, 30 as relSeq
union all 
select 40 as distance_key, '15-20 Mi' as descr, 15 as minDistance, 20 as maxDistance, 40 as relSeq
union all 
select 50 as distance_key, '20-25 Mi' as descr, 20 as minDistance, 25 as maxDistance, 50 as relSeq
union all 
select 60 as distance_key, '25-30 Mi' as descr, 25 as minDistance, 30 as maxDistance, 60 as relSeq
union all 
select 70 as distance_key, '30-35 Mi' as descr, 30 as minDistance, 35 as maxDistance, 70 as relSeq
union all 
select 80 as distance_key, '35-40 Mi' as descr, 35 as minDistance, 40 as maxDistance, 80 as relSeq
union all 
select 900 as distance_key, 'Over 40 Mi' as descr, 40 as minDistance, 32767 as maxDistance, 900 as relSeq
```

