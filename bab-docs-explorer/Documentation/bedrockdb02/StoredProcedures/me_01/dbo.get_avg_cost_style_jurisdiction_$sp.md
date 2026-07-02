# dbo.get_avg_cost_style_jurisdiction_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_avg_cost_style_jurisdiction_$sp"]
    dbo_get_last_net_final_po_cost__sp(["dbo.get_last_net_final_po_cost_$sp"]) --> SP
    dbo_ib_inventory(["dbo.ib_inventory"]) --> SP
    dbo_ib_inventory_total(["dbo.ib_inventory_total"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_last_net_final_po_cost_$sp |
| dbo.ib_inventory |
| dbo.ib_inventory_total |
| dbo.location |
| dbo.sku |

## Stored Procedure Code

```sql
-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Procedure
-----------------------------------------------------------------------------------------------------------------------------

CREATE PROCEDURE dbo.get_avg_cost_style_jurisdiction_$sp

	 @Date AS SMALLDATETIME = NULL

AS

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON


/*
	Get dynamic average cost by style/jurisdiction
	Called by get_avg_cost_$sp and get_avg_cost_sku_jurisdiction_$sp

	History:
	9/30/2015	Ivan Dimitrov		143201 - Sale-customer order transaction 605 does not pick the cost from the virtual transfer when calculating average cost
	10/14/2015	Ivan Dimitrov		144440 - Sales posting not calculating average cost correctly when on hand cost is 0, units > 0
	1/21/2016	Ivan Dimitrov		155050 - When there are transactions after the count date average cost calculation is wrong
*/

CREATE TABLE dbo.#temp_style_jurisdiction
	(
		jurisdiction_id SMALLINT NULL
		,style_id DECIMAL (12, 0) NULL
	)

INSERT INTO dbo.#temp_style_jurisdiction
	(
		jurisdiction_id
		,style_id
	)
SELECT DISTINCT
	jurisdiction_id
	,style_id
FROM
	dbo.#temp_wrk_avg_cost_lookup

INSERT INTO dbo.#temp_avg_costs

	(
		location_id
		,sku_id
		,avg_cost
		,avg_cost_local
		,sum_units
		,sum_cost
		,sum_cost_local
	)

SELECT
	TWACL.location_id
	,TWACL.sku_id
	,SQAV.avg_cost
	,SQAV.avg_cost_local
	,SQAV.sum_units
	,SQAV.sum_cost
	,SQAV.sum_cost_local
FROM
	dbo.#temp_wrk_avg_cost_lookup	TWACL
	INNER JOIN

		(
			SELECT
				TSL.style_id
				,TSL.jurisdiction_id
				,SUM(IBIT.total_on_hand_cost - ISNULL (sqMV.transaction_cost, 0)) / SUM(CONVERT(BIGINT,IBIT.total_on_hand_units - ISNULL (sqMV.transaction_units, 0))) AS avg_cost
				,SUM(IBIT.total_on_hand_cost_local - ISNULL (sqMV.transaction_cost_local, 0)) / SUM(CONVERT(BIGINT,IBIT.total_on_hand_units - ISNULL (sqMV.transaction_units, 0))) AS avg_cost_local
				,SUM(CONVERT(BIGINT,IBIT.total_on_hand_units - ISNULL (sqMV.transaction_units, 0))) as sum_units
				,SUM(IBIT.total_on_hand_cost - ISNULL (sqMV.transaction_cost, 0)) as sum_cost
				,SUM(IBIT.total_on_hand_cost_local - ISNULL (sqMV.transaction_cost_local, 0)) as sum_cost_local
			FROM
				(SELECT sku_id, location_id, SUM(total_on_hand_units) as total_on_hand_units,
						SUM(total_on_hand_cost) as total_on_hand_cost, SUM(total_on_hand_cost_local) as total_on_hand_cost_local
						FROM ib_inventory_total
						GROUP BY sku_id, location_id) IBIT
				INNER JOIN sku K ON IBIT.sku_id = K.sku_id
				INNER JOIN location L ON IBIT.location_id = L.location_id
				INNER JOIN dbo.#temp_style_jurisdiction TSL ON K.style_id = TSL.style_id AND L.jurisdiction_id = TSL.jurisdiction_id
				LEFT JOIN

					(
						SELECT
							 IBI.sku_id
							,IBI.location_id
							,SUM (IBI.transaction_cost) AS transaction_cost
							,SUM (IBI.transaction_cost_local) AS transaction_cost_local
							,SUM (IBI.transaction_units) AS transaction_units
					FROM
						dbo.ib_inventory IBI
					WHERE
						IBI.transaction_date > @Date
					GROUP BY
						 IBI.sku_id
						,IBI.location_id
					) sqMV ON sqMV.location_id = IBIT.location_id AND sqMV.sku_id = IBIT.sku_id

			GROUP BY
				TSL.style_id, TSL.jurisdiction_id
			HAVING
				SUM(IBIT.total_on_hand_cost - ISNULL (sqMV.transaction_cost, 0)) >= 0
				AND SUM(CONVERT(BIGINT,IBIT.total_on_hand_units - ISNULL (sqMV.transaction_units, 0))) > 0
		) SQAV ON TWACL.style_id = SQAV.style_id AND TWACL.jurisdiction_id = SQAV.jurisdiction_id

WHERE
	NOT EXISTS
		(
			SELECT *
			FROM
				dbo.#temp_avg_costs D
			WHERE
				TWACL.sku_id = D.sku_id
				AND TWACL.location_id = D.location_id
		)

EXEC dbo.get_last_net_final_po_cost_$sp
```

