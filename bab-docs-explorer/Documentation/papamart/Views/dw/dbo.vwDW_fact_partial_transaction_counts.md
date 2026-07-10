# dbo.vwDW_fact_partial_transaction_counts

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_fact_partial_transaction_counts"]
    dbo_partial_transaction_count_facts(["dbo.partial_transaction_count_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.partial_transaction_count_facts |

## View Code

```sql
CREATE VIEW vwDW_fact_partial_transaction_count
AS

	SELECT
		[store_key]
		,[date_key]
		,[partial_transaction_count]
	FROM [dw].[dbo].[partial_transaction_count_facts]
```

