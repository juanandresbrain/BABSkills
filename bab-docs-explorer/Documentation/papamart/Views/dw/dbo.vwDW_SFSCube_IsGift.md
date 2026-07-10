# dbo.vwDW_SFSCube_IsGift

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_IsGift"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_IsGift]
AS
SELECT     cast(1 as bit) as isGiftInd, cast('Gift' as varchar(50)) as Descr
union all
select cast (0 as bit), 'Not Gift'
```

