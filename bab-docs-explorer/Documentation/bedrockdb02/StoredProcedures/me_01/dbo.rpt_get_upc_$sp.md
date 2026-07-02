# dbo.rpt_get_upc_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_upc_$sp"]
    dbo_type_sku_list(["dbo.type_sku_list"]) --> SP
    dbo_upc(["dbo.upc"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.type_sku_list |
| dbo.upc |

## Stored Procedure Code

```sql
/*
For each size, this is set to the vendor UPC Number. 

If more than 1 vendor UPC is found, then it will display the UPC with latest activity date.
If more than 1 vendor UPC with the same activity date is found, then it will display the UPC with the latest Activation date.
If more than 1 vendor UPC with the same Activation date is found, then it will display the UPC that is the highest value (i.e. MAX(dbo.upc.upc_number))

If a vendor UPC is not found, then display the latest in-house UPC (if one exists)
If more than 1 in-house UPC is found, then it will display the UPC with latest activity date
If more than 1 in-house UPC with the same activity date is found, then it will display the UPC that is the highest value (i.e. MAX (dbo.upc.upc_number))
*/
CREATE PROCEDURE [dbo].[rpt_get_upc_$sp]
	(
		@type_sku_list AS type_sku_list READONLY
	)
AS

DECLARE @sku_upc_list_output AS TABLE
	(
		 sku_id DECIMAL (13, 0) NULL
		,upc_number NVARCHAR (14) NULL
		,upc_type TINYINT NULL
	)

INSERT INTO @sku_upc_list_output
	(
		 sku_id
		,upc_number
		,upc_type
	)
SELECT
	 a.sku_id
	,a.upc_number
	,a.upc_type
FROM
	(
		SELECT
			 upc.sku_id
			,upc.upc_number
			,upc.upc_type
			,RANK () OVER
						(
							PARTITION BY
								upc.sku_id
							ORDER BY
								 upc.last_activity_date DESC
								,upc.activation_date DESC
								,upc.upc_number DESC
						) AS rank_filter
			FROM
				dbo.upc
			WHERE
				upc.upc_type = 1
				AND EXISTS
					(
						SELECT
							*
						FROM
							@type_sku_list stt
						WHERE
							stt.sku_id = upc.sku_id
					)
	) a
WHERE
	a.rank_filter = 1

INSERT INTO @sku_upc_list_output
	(
		 sku_id
		,upc_number
		,upc_type
	)
SELECT
	 a.sku_id
	,a.upc_number
	,a.upc_type
FROM
	(
		SELECT
			 upc.sku_id
			,upc.upc_number
			,upc.upc_type
			,RANK () OVER
						(
							PARTITION BY
								upc.sku_id
							ORDER BY
								 upc.last_activity_date DESC
								,upc.upc_number DESC
						) AS rank_filter
			FROM
				dbo.upc
			WHERE
				upc.upc_type = 2
				AND EXISTS
					(
						SELECT
							*
						FROM
							@type_sku_list stt
						WHERE
							stt.sku_id = upc.sku_id
					)
				AND NOT EXISTS
					(
						SELECT
							*
						FROM
							@sku_upc_list_output lstOut
						WHERE
							lstOut.sku_id = upc.sku_id
					)
	) a
WHERE
	a.rank_filter = 1

SELECT
	lstOut.*
FROM
	@sku_upc_list_output lstOut
```

