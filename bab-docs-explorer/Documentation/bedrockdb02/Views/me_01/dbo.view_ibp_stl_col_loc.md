# dbo.view_ibp_stl_col_loc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_ibp_stl_col_loc"]
    dbo_ib_price(["dbo.ib_price"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_price |

## View Code

```sql
create view dbo.view_ibp_stl_col_loc 



AS

SELECT
	ib_price.ib_price_id,
	ib_price.jurisdiction_id,
	ib_price.style_id,
	ib_price.color_id,
	ib_price.location_id,
	ib_price.effective_date,
	ib_price.start_date,
	ib_price.document_number,
	ib_price.valuation_retail_price,
	ib_price.selling_retail_price,
	ib_price.price_status_id,
	ib_price.price_change_type
FROM
	dbo.ib_price
WHERE
	ib_price.temp_price_flag = 0 
	AND ib_price.color_id IS NOT NULL
	AND ib_price.location_id IS NOT NULL
	AND ib_price.effective_date IS NOT NULL
```

