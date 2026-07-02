# dbo.sp_delete_log_shipping_secondary

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_delete_log_shipping_secondary"]
    dbo_log_shipping_secondaries(["dbo.log_shipping_secondaries"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.log_shipping_secondaries |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_delete_log_shipping_secondary 
  @secondary_server_name   sysname,
  @secondary_database_name sysname
AS BEGIN
  SET NOCOUNT ON
  DELETE FROM msdb.dbo.log_shipping_secondaries WHERE 
    secondary_server_name   = @secondary_server_name AND
    secondary_database_name = @secondary_database_name
END
```

