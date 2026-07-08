# dbo.DeleteActiveSubscription

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteActiveSubscription"]
    ActiveSubscriptions(["ActiveSubscriptions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ActiveSubscriptions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteActiveSubscription]
@ActiveID uniqueidentifier
AS

delete from ActiveSubscriptions where ActiveID = @ActiveID
```

