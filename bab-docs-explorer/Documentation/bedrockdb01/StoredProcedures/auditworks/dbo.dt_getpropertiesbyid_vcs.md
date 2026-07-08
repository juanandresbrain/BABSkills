# dbo.dt_getpropertiesbyid_vcs

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dt_getpropertiesbyid_vcs"]
    dbo_dtproperties(["dbo.dtproperties"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dtproperties |

## Stored Procedure Code

```sql
create procedure dbo.dt_getpropertiesbyid_vcs
    @id       int,
    @property varchar(64),
    @value    varchar(255) = NULL OUT

as

    set nocount on

    select @value = (
        select value
                from dbo.dtproperties
                where @id=objectid and @property=property
                )
```

