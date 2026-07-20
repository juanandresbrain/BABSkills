# dbo.tender_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tender_facts"]
    dbo_tender_facts(["dbo.tender_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tender_facts |

## View Code

```sql
CREATE   VIEW [dbo].[tender_facts] AS SELECT tender_facts_key, transaction_id, tender_key, store_key, date_key, tender_amt, tender_count, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID FROM LH_Mart.dbo.tender_facts;
```

