# dbo.franchisee_store_count_staging

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchisee_store_count_staging"]
    dbo_franchisee_store_count_staging(["dbo.franchisee_store_count_staging"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchisee_store_count_staging |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchisee_store_count_staging]
AS
    SELECT [region_key] COLLATE Latin1_General_CI_AS AS [region_key], [date_key], [actual_date], [fiscal_year], [fiscal_week], [numStores]
    FROM LH_Staging.[dbo].[franchisee_store_count_staging]
```

