# dbo.GetUserIDByName

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetUserIDByName"]
    Users(["Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Users |

## Stored Procedure Code

```sql
-- looks up any user name by its User Name, if not it creates a regular user
CREATE PROCEDURE [dbo].[GetUserIDByName]
@UserName nvarchar(260),
@AuthType int,
@UserID uniqueidentifier OUTPUT
AS
SELECT @UserID = (SELECT UserID FROM Users WHERE UserName = @UserName AND AuthType = @AuthType)
IF @UserID IS NULL
   BEGIN
      SET @UserID = newid()
      INSERT INTO Users
      (UserID, Sid, UserType, AuthType, UserName)
      VALUES 
      (@UserID, NULL, 0,    @AuthType, @UserName)
   END
```

