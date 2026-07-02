# dbo.Web_AddUser

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Web_AddUser"]
    dbo_Lg_Identification(["dbo.Lg_Identification"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
    dbo_Sv_User(["dbo.Sv_User"]) --> SP
    dbo_Sv_UserTopic(["dbo.Sv_UserTopic"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Lg_Identification |
| dbo.Sv_GetNextID |
| dbo.Sv_User |
| dbo.Sv_UserTopic |

## Stored Procedure Code

```sql

```

