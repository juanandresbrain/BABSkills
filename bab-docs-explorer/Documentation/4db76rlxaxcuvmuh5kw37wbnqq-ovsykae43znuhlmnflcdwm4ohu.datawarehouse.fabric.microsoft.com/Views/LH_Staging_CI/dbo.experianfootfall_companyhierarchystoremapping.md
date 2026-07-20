# dbo.experianfootfall_companyhierarchystoremapping

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.experianfootfall_companyhierarchystoremapping"]
    dbo_experianfootfall_companyhierarchystoremapping(["dbo.experianfootfall_companyhierarchystoremapping"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.experianfootfall_companyhierarchystoremapping |

## View Code

```sql
; CREATE   VIEW [dbo].[experianfootfall_companyhierarchystoremapping] AS SELECT [store_key], [SiteIdentity], [IsShopperTrak], [IsFootFall], [IsCurrentlyOffline], [CompanyID], [HierarchyID], [NodeName] COLLATE Latin1_General_CI_AS AS [NodeName], [CurrencyCode] COLLATE Latin1_General_CI_AS AS [CurrencyCode], [Updt_dt] FROM [dbo].[experianfootfall_companyhierarchystoremapping]
```

