# dbo.franchisee_store_count_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchisee_store_count_facts"]
    dbo_franchisee_store_count_facts(["dbo.franchisee_store_count_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchisee_store_count_facts |

## View Code

```sql
; CREATE   VIEW [dbo].[franchisee_store_count_facts] AS     SELECT [weekending_date_key], [region_key] COLLATE Latin1_General_CI_AS AS [region_key], [store_count], [src_extrct_dt], [upd_dt], [etl_log_id], [etl_evnt_id]     FROM [dbo].[franchisee_store_count_facts]
```

