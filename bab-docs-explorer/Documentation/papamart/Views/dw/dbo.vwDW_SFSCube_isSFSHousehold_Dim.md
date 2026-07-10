# dbo.vwDW_SFSCube_isSFSHousehold_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_isSFSHousehold_Dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW dbo.vwDW_SFSCube_isSFSHousehold_Dim
AS
SELECT   cast (1 as bit) as isSFSHousehold, cast('SFS Household' as varchar(50)) as Descr  
union all
SELECT   cast (0 as bit) as isSFSHousehold, cast('NOT SFS Household' as varchar(50)) as Descr
```

