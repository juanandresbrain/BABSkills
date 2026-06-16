# dbo.sp_MSrepl_startup

**Database:** master  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MSrepl_startup"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
create procedure dbo.sp_MSrepl_startup
as
    exec sys.sp_MSrepl_startup_internal
```

