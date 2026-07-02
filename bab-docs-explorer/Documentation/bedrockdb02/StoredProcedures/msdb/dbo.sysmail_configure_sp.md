# dbo.sysmail_configure_sp

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sysmail_configure_sp"]
    dbo_sysmail_configuration(["dbo.sysmail_configuration"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysmail_configuration |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sysmail_configure_sp
   @parameter_name nvarchar(256),
   @parameter_value nvarchar(256),
   @description nvarchar(256) = NULL
AS
   SET NOCOUNT ON
   
   IF (@description IS NOT NULL)
      UPDATE msdb.dbo.sysmail_configuration
      SET paramvalue=@parameter_value, description=@description
      WHERE paramname=@parameter_name
   ELSE
      UPDATE msdb.dbo.sysmail_configuration
      SET paramvalue=@parameter_value
      WHERE paramname=@parameter_name

   RETURN(0)
```

