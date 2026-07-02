# dbo.Sv_Admin_AddUserToSv18

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_Admin_AddUserToSv18"]
    dbo_Lg_Identification(["dbo.Lg_Identification"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Sv_User(["dbo.Sv_User"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Lg_Identification |
| dbo.Sv_GetNextID |
| dbo.Sv_User |

## Stored Procedure Code

```sql

```

