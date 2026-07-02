# dbo.sp_sysdac_ensure_dac_creator

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysdac_ensure_dac_creator"]
    dbo_fn_sysdac_is_dac_creator(["dbo.fn_sysdac_is_dac_creator"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.fn_sysdac_is_dac_creator |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_sysdac_ensure_dac_creator
as
BEGIN
    -- only users that can create a dac can add parts
    IF (dbo.fn_sysdac_is_dac_creator() != 1)
    BEGIN
        RAISERROR(36010, -1, -1);
        RETURN(1); -- failure
    END
END
```

