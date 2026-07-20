# dbo.salesplan_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.salesplan_facts"]
    dbo_salesplan_facts(["dbo.salesplan_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.salesplan_facts |

## View Code

```sql
CREATE   VIEW [dbo].[salesplan_facts] AS SELECT salesplan_facts_key, store_key, date_key, currency_key, amount FROM LH_Mart.dbo.salesplan_facts;
```

