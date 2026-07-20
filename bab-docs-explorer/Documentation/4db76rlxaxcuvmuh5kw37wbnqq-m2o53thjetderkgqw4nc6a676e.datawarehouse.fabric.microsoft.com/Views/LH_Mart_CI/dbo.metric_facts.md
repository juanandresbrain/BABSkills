# dbo.metric_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.metric_facts"]
    dbo_metric_facts(["dbo.metric_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.metric_facts |

## View Code

```sql
CREATE   VIEW [dbo].[metric_facts] AS SELECT metric_facts_key, metric_dim_key, store_key, date_key, amount, ly_date_key, ly_amount FROM LH_Mart.dbo.metric_facts;
```

