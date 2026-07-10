# dbo.vwDW_fact_kiosk

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_fact_kiosk"]
    dbo_transaction_kiosk_facts(["dbo.transaction_kiosk_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_kiosk_facts |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_fact_kiosk]
AS

	SELECT
		CASE WHEN customer_geography_key = 0 THEN NULL ELSE customer_geography_key END AS customer_geography_key
		,CASE WHEN customer_demographics_key IS NULL THEN 0 ELSE customer_demographics_key END AS customer_demographics_key
		,store_key
		,date_key
		,guest_type_key
		,purpose_key
		,CASE WHEN product_key = 0 THEN NULL ELSE CAST(product_key AS varchar) END AS product_key
		,transaction_id
	FROM dbo.transaction_kiosk_facts WITH (NOLOCK, INDEX(idxN_U_transaction_kiosk_facts_date_key))
```

