# dbo.CreateNewActiveSubscription

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateNewActiveSubscription"]
    ActiveSubscriptions(["ActiveSubscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ActiveSubscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CreateNewActiveSubscription]
@ActiveID uniqueidentifier,
@SubscriptionID uniqueidentifier
AS


-- Insert into the activesubscription table
insert into [ActiveSubscriptions] 
    (
    [ActiveID], 
    [SubscriptionID],
    [TotalNotifications],
    [TotalSuccesses],
    [TotalFailures]
    )
values
    (
    @ActiveID,
    @SubscriptionID,
    NULL,
    0,
    0
    )
```

