# dbo.UpdateSubscriptionLastRunInfo

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateSubscriptionLastRunInfo"]
    Subscriptions(["Subscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Subscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateSubscriptionLastRunInfo]
@SubscriptionID uniqueidentifier,
@Flags int,
@LastRunTime datetime,
@LastStatus nvarchar(260)
AS

update Subscriptions set
        [InactiveFlags] = @Flags,
        [LastRunTime] = @LastRunTime,
        [LastStatus] = @LastStatus
where
    [SubscriptionID] = @SubscriptionID
```

