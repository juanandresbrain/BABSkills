# dbo.SetNotificationAttempt

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetNotificationAttempt"]
    Notifications(["Notifications"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Notifications |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetNotificationAttempt] 
@Attempt int,
@SecondsToAdd int,
@NotificationID uniqueidentifier
AS

update 
    [Notifications] 
set 
    [ProcessStart] = NULL, 
    [Attempt] = @Attempt, 
    [ProcessAfter] = DateAdd(second, @SecondsToAdd, GetUtcDate())
where
    [NotificationID] = @NotificationID
```

