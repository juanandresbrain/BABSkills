# dbo.franchisee_store_comp_dates_staging

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchisee_store_comp_dates_staging"]
    dbo_franchisee_store_comp_dates_staging(["dbo.franchisee_store_comp_dates_staging"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchisee_store_comp_dates_staging |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchisee_store_comp_dates_staging]
AS
    SELECT [id], [code] COLLATE Latin1_General_CI_AS AS [code], [start_date_key], [end_date_key]
    FROM LH_Staging.[dbo].[franchisee_store_comp_dates_staging]
```

