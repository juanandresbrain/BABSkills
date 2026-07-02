# dbo.sysmail_help_configure_sp

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sysmail_help_configure_sp"]
    dbo_sysmail_configuration(["dbo.sysmail_configuration"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysmail_configuration |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sysmail_help_configure_sp
   @parameter_name nvarchar(256) = NULL
AS
   SET NOCOUNT ON

    SELECT paramname, paramvalue, description
    FROM msdb.dbo.sysmail_configuration
    WHERE paramname = ISNULL(@parameter_name, paramname)

    RETURN(0)
```

