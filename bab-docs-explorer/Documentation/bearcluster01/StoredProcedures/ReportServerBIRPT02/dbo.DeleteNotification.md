# dbo.DeleteNotification

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteNotification"]
    dbo_Notifications(["dbo.Notifications"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Notifications |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteNotification]
@ID uniqueidentifier
AS
delete from [Notifications] where [NotificationID] = @ID
```

