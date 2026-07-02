# dbo.SetReencryptedUserServiceToken

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetReencryptedUserServiceToken"]
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetReencryptedUserServiceToken]
@UserID uniqueidentifier,
@ServiceToken ntext
AS

UPDATE [dbo].[Users]
SET [ServiceToken] = @ServiceToken
WHERE [UserID] = @UserID
```

