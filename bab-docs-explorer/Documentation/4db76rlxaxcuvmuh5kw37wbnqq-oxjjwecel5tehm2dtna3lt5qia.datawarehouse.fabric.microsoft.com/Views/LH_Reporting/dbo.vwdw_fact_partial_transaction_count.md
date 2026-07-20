# dbo.vwdw_fact_partial_transaction_count

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_fact_partial_transaction_count"]
    dbo_partial_transaction_count_facts(["dbo.partial_transaction_count_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.partial_transaction_count_facts |

## View Code

```sql
CREATE VIEW vwdw_fact_partial_transaction_count  
 AS  
  SELECT  TOp 1
    store_key
   ,date_key  
   ,partial_transaction_count
  FROM LH_Mart.dbo.partial_transaction_count_facts
```

