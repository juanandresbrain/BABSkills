# dbo.vwWMS_3PL_InventoryStage

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwWMS_3PL_InventoryStage"]
    dbo_NightlyWhseInventory(["dbo.NightlyWhseInventory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NightlyWhseInventory |

## View Code

```sql
CREATE VIEW [dbo].[vwWMS_3PL_InventoryStage]
AS
select 
	cast(style_code as varchar(6)) as ItemNumber,
	sum(qty) as WhseQty,
	location_code as LocationCode,
	cast(load_date as date) as InventoryDate,
	cast(
		case 
			when location_code='2970' then 2110
			when location_code in ('3970','8502','8505') then 3001
			when location_code IN ('3980','9942') then 1200
			when location_code='0960' then 1100
		end as nvarchar(4)
		) as Entity

from NightlyWhseInventory 
where cast(load_date as date)=cast(getdate() as date)
	AND (
		(
			location_code in  ('2970','3970','3980','0960','8505','8502','9942')
			AND cast(getdate() as date) < '2025-11-30'
		)
	  OR
		(
		location_code in  ('2970','3970','0960','8505','8502') -- 3980(9941) and 9942 removed per BearAssist #92464:9941 and 9942 should be included on the sync for 11/29 but not for 11/30 and after
		AND cast(getdate() as date) > '2025-11-29' 
		)
	  )
--and location_code='0960'
--and style_code='018957'
group by 
	cast(style_code as varchar(6)),
	location_code,
cast(load_date as date)
--order by 
--cast(
--		case 
--			when location_code='2970' then 2110
--			when location_code in ('3970','8502','8505') then 3001
--			when location_code IN ('3980','9942') then 1200
--			when location_code='0960' then 1100
--		end as nvarchar(4)
--		),
--	location_code, 
--	style_code
```

