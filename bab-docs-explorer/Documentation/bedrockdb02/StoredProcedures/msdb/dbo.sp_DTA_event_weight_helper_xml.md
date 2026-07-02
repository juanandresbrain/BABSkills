# dbo.sp_DTA_event_weight_helper_xml

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_event_weight_helper_xml"]
    dbo_DTA_reports_query(["dbo.DTA_reports_query"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_query |

## Stored Procedure Code

```sql
create procedure sp_DTA_event_weight_helper_xml 
	@SessionID int 
as 
begin
	select 1            as Tag, 
			NULL          as Parent,
			'' as [EventWeightReport!1!!element],
			NULL as [EventDetails!2!EventString!ELEMENT] ,
			NULL as [EventDetails!2!Weight!ELEMENT]
	union all

	select 2         as Tag, 
			1         as Parent,
			NULL as [QueryCost!1!!element],
			EventString as [EventDetails!2!EventString!ELEMENT] ,
			CAST(EventWeight as decimal(38,2)) as [EventDetails!2!Weight!ELEMENT]
			from [msdb].[dbo].[DTA_reports_query]
			where SessionID=@SessionID and EventWeight>0
	order by Tag,[EventDetails!2!Weight!ELEMENT] desc  
	FOR XML EXPLICIT	
end
```

