# dbo.GetUserServiceTokenForReencryption

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetUserServiceTokenForReencryption"]
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetUserServiceTokenForReencryption]
@UserID as uniqueidentifier
AS

SELECT [ServiceToken]
FROM [dbo].[Users]
WHERE [UserID] = @UserID
```

