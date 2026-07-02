# dbo.sp_DTA_query_cost_helper_relational

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_DTA_query_cost_helper_relational"]
    dbo_DTA_reports_query(["dbo.DTA_reports_query"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DTA_reports_query |

## Stored Procedure Code

```sql
create procedure sp_DTA_query_cost_helper_relational
			@SessionID		int
			as
			begin 	select "Statement Id" = QueryID, "Statement String" = StatementString, "Percent Improvement" = 	
					CASE
						WHEN CurrentCost = 0 THEN 0.00
						WHEN CurrentCost <> 0 THEN
						CAST((100.0*(CurrentCost - RecommendedCost)/CurrentCost) as decimal (20,2))
					end , "Statement Type" = CASE 
							WHEN StatementType = 0 THEN 'Select'
							WHEN StatementType = 1 THEN 'Update'
							WHEN StatementType = 2 THEN 'Insert'
							WHEN StatementType = 3 THEN 'Delete'
							WHEN StatementType = 4 THEN 'Merge'
							end 	from [msdb].[dbo].[DTA_reports_query]
					where SessionID=@SessionID
					order by "Percent Improvement" desc  end
```

