# dbo.DeleteNotification

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteNotification"]
    Notifications(["Notifications"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Notifications |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteNotification] 
@ID uniqueidentifier
AS
delete from [Notifications] where [NotificationID] = @ID
```

