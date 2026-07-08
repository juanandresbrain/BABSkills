# dbo.sp_MSremove_published_jobs

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MSremove_published_jobs"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_MSremove_published_jobs
@server sysname,
@database sysname
AS
    -- 6.5 publisher and 7.0 publisher will call this
    -- publisher_database_id will be drop in sp_MSdrop_publication.
    return(0)
```

