# dbo.sp_DTA_event_weight_helper_relational

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_event_weight_helper_relational"]
    dbo_DTA_reports_query(["dbo.DTA_reports_query"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_query |

## Stored Procedure Code

```sql
create procedure sp_DTA_event_weight_helper_relational
			@SessionID		int
			as
			begin	select "Event String"= EventString, "Weight" = CAST(EventWeight as decimal(38,2)) 	from [msdb].[dbo].[DTA_reports_query]
					where SessionID=@SessionID and EventWeight>0
					order by EventWeight desc  end
```

