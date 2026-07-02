# dbo.sp_MSrepl_startup

**Database:** master  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MSrepl_startup"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
create procedure dbo.sp_MSrepl_startup
as
    exec sys.sp_MSrepl_startup_internal
```

