# dbo.SetNotificationAttempt

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetNotificationAttempt"]
    dbo_Notifications(["dbo.Notifications"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Notifications |

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

