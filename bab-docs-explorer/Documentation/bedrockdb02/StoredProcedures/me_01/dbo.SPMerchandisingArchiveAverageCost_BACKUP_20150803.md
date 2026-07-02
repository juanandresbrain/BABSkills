# dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803"]
    dbo_ib_inventory(["dbo.ib_inventory"]) --> SP
    dbo_keith_average_cost(["dbo.keith_average_cost"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_detail(["dbo.style_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_inventory |
| dbo.keith_average_cost |
| dbo.sku |
| dbo.style |
| dbo.style_detail |

## Stored Procedure Code

```sql
create procedure [dbo].[SPMerchandisingArchiveAverageCost_BACKUP_20150803]
as
set nocount on
-- =====================================================================================================
-- Name: SPMerchandisingArchiveAverageCost
--
-- Description:Build Average Cost Table.
-- Revision History
--		Name:			Date:			Comments: This Proc replaces existing DTS pkg on Beehive called Archive_Average_Cost_V1
--		Dan Tweedie 	    03/02/2015		Created proc.	
-- =====================================================================================================

TRUNCATE TABLE keith_average_cost

INSERT INTO keith_average_cost
SELECT s.style_code,
	s.short_desc,
	CASE 
		WHEN sum(ii.transaction_cost) = 0
			OR sum(ii.transaction_units) = 0
			THEN 0.00
		WHEN sum(ii.transaction_units) < 0
			THEN sd.last_net_final_po_cost
		ELSE sum(ii.transaction_cost) / sum(ii.transaction_units)
		END average_cost
FROM (
	SELECT sku_id,
		transaction_units,
		transaction_cost,
		transaction_date
	FROM ib_inventory(NOLOCK)
	) ii
INNER JOIN sku sk(NOLOCK) ON ii.sku_id = sk.sku_id
INNER JOIN style s(NOLOCK) ON sk.style_id = s.style_id
INNER JOIN style_detail sd(NOLOCK) ON s.style_id = sd.style_id
WHERE cast(convert(VARCHAR(10), ii.transaction_date, 101) AS DATETIME) <= cast(convert(VARCHAR(10), getdate(), 101) AS DATETIME) --'2006-10-09'
GROUP BY s.style_code, s.short_desc, sd.last_net_final_po_cost
```

