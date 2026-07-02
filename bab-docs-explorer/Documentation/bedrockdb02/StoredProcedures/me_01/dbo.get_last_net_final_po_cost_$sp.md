# dbo.get_last_net_final_po_cost_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_last_net_final_po_cost_$sp"]
    dbo_style_detail(["dbo.style_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_detail |

## Stored Procedure Code

```sql
-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Procedure
-----------------------------------------------------------------------------------------------------------------------------

CREATE PROCEDURE dbo.get_last_net_final_po_cost_$sp

	 @Date AS SMALLDATETIME = NULL

AS

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON

INSERT INTO dbo.#temp_avg_costs

	(
		location_id
		,sku_id
		,avg_cost
		,avg_cost_local
	)

SELECT
	TWACL.location_id
	,TWACL.sku_id
	,SD.last_net_final_po_cost AS avg_cost
	,SD.last_net_final_po_cost / TCR.cost_rate AS avg_cost_local
FROM
	dbo.#temp_wrk_avg_cost_lookup TWACL
	INNER JOIN dbo.style_detail SD ON TWACL.style_id = SD.style_id
	INNER JOIN dbo.#temp_cost_rates TCR ON TCR.jurisdiction_id = TWACL.jurisdiction_id
WHERE
	NOT EXISTS
		( 
			SELECT 1
			FROM
				dbo.#temp_avg_costs D
			WHERE
				TWACL.sku_id = D.sku_id
				AND TWACL.location_id = D.location_id 
		)
```

