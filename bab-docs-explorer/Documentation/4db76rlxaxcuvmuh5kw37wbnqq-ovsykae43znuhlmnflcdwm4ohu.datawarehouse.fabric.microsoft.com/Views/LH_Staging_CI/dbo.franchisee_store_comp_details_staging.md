# dbo.franchisee_store_comp_details_staging

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchisee_store_comp_details_staging"]
    dbo_franchisee_store_comp_details_staging(["dbo.franchisee_store_comp_details_staging"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchisee_store_comp_details_staging |

## View Code

```sql
; CREATE   VIEW [dbo].[franchisee_store_comp_details_staging] AS SELECT [id], [FranchiseeName] COLLATE Latin1_General_CI_AS AS [FranchiseeName], [RegionName] COLLATE Latin1_General_CI_AS AS [RegionName], [BearitoryName] COLLATE Latin1_General_CI_AS AS [BearitoryName], [Country] COLLATE Latin1_General_CI_AS AS [Country], [CountryName] COLLATE Latin1_General_CI_AS AS [CountryName], [StoreNo] COLLATE Latin1_General_CI_AS AS [StoreNo], [store_name] COLLATE Latin1_General_CI_AS AS [store_name], [openDate], [closeDate], [Language] COLLATE Latin1_General_CI_AS AS [Language] FROM [dbo].[franchisee_store_comp_details_staging]
```

