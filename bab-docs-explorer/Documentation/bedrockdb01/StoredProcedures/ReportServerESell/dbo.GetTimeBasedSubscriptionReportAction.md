# dbo.GetTimeBasedSubscriptionReportAction

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetTimeBasedSubscriptionReportAction"]
    Catalog(["Catalog"]) --> SP
    ReportSchedule(["ReportSchedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Catalog |
| ReportSchedule |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetTimeBasedSubscriptionReportAction]
@SubscriptionID uniqueidentifier
AS
select 
        RS.[ReportAction],
        RS.[ScheduleID],
        RS.[ReportID],
        RS.[SubscriptionID],
        C.[Path],
        C.[Type]
from
    [ReportSchedule] RS Inner join [Catalog] C on RS.[ReportID] = C.[ItemID]
where
    RS.[SubscriptionID] = @SubscriptionID
```

