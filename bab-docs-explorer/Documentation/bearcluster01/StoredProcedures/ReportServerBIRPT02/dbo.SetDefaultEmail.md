# dbo.SetDefaultEmail

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetDefaultEmail"]
    dbo_UserContactInfo(["dbo.UserContactInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UserContactInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetDefaultEmail]
    @UserID uniqueidentifier,
    @DefaultEmailAddress nvarchar(256)
AS
BEGIN
    IF EXISTS (SELECT * FROM UserContactInfo WHERE UserID = @UserID) BEGIN
        UPDATE UserContactInfo SET
        DefaultEmailAddress = @DefaultEmailAddress
        WHERE UserID=@UserID
    END ELSE BEGIN
        INSERT
        INTO [UserContactInfo] (UserID, DefaultEmailAddress)
        VALUES (@UserID, @DefaultEmailAddress)
    END
END
```

