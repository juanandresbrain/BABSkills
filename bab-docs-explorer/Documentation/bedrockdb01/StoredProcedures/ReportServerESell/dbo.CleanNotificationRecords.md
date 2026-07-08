# dbo.CleanNotificationRecords

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanNotificationRecords"]
    Notifications(["Notifications"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Notifications |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanNotificationRecords] 
@MaxAgeMinutes int
AS
-- Reset all notifications which have been add over n minutes ago
Update [Notifications] set [ProcessStart] = NULL, [ProcessHeartbeat] = NULL, [Attempt] = 1
where [NotificationID] in
   ( SELECT [NotificationID]
     FROM [Notifications]
     WHERE [ProcessHeartbeat] < DATEADD(minute, -(@MaxAgeMinutes), GETUTCDATE()) and [Attempt] is NULL )

Update [Notifications] set [ProcessStart] = NULL, [ProcessHeartbeat] = NULL, [Attempt] = [Attempt] + 1
where [NotificationID] in
   ( SELECT [NotificationID]
     FROM [Notifications]
     WHERE [ProcessHeartbeat] < DATEADD(minute, -(@MaxAgeMinutes), GETUTCDATE()) and [Attempt] is not NULL )
```

