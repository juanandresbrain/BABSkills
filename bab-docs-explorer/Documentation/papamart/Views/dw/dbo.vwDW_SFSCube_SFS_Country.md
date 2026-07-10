# dbo.vwDW_SFSCube_SFS_Country

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_SFS_Country"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.vwDW_SFSCube_SFS_Country
AS
SELECT cast('US' as varchar(3)) as SFS_Country, cast(10 as smallint) as relSEQ
union all
select 'CAN' , 20
union all
select 'UK', 30
union all
select 'N/A', 999
```

