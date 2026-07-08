# dbo.sp_MSget_repl_version

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MSget_repl_version"]
    MSrepl_version(["MSrepl_version"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| MSrepl_version |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_MSget_repl_version
@major_version int = 0 OUTPUT,
@minor_version int = 0 OUTPUT,
@revision int = 0 OUTPUT

as
SELECT @major_version = major_version,
       @minor_version = minor_version,
       @revision = revision FROM MSrepl_version
```

