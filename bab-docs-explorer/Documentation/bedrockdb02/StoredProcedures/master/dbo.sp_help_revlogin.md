# dbo.sp_help_revlogin

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_help_revlogin"]
    dbo_sp_hexadecimal(["dbo.sp_hexadecimal"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_hexadecimal |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_help_revlogin @login_name sysname = NULL AS
```

