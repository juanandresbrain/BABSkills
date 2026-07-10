# dbo.vwDW_SFSCube_IsParty

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_IsParty"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_IsParty]
AS
SELECT     cast(1 as tinyint) as isParty, cast('Party' as varchar(50)) as Descr
union all
select cast (0 AS tinyint), 'Not Party'
```

