# dbo.GetDefaultEmail

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDefaultEmail"]
    dbo_UserContactInfo(["dbo.UserContactInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UserContactInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDefaultEmail]
    @UserID uniqueidentifier
AS
BEGIN
    SELECT TOP(1)
        U.[DefaultEmailAddress]
    FROM
        [UserContactInfo] as U
    WHERE
        U.UserID = @UserID
END
```

