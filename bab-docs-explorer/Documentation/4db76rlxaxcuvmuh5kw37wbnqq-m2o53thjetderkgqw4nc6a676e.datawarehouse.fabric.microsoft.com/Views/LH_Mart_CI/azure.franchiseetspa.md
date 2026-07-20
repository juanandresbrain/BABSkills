# azure.franchiseetspa

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.franchiseetspa"]
    dbo_azure_franchiseetspa(["dbo.azure_franchiseetspa"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.azure_franchiseetspa |

## View Code

```sql
CREATE     VIEW [azure].[franchiseetspa] AS SELECT WeekEndingDate, FranchiseeCountry COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [FranchiseeCountry], Dept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [Dept], DptRnk, DptRnkPW, CGrpRnk, CGrpRnkPW, YTDRnk, KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [KeyStory], ConsGrp COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [ConsGrp], Style# COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [Style#], StyleDesc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [StyleDesc], NonPromoRtl, MSTAT COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS [MSTAT], SlsULW, SlsUPW, SlsU2PW, SlsUYTD, SlsR$, AUR, Velcty, InStrST, StoreOnHand, WebStoresOnHand, WarehouseOnHand, TotalOnHand, WeeksOfSupply, DueByJAN, DueByFEB, DueByMAR, DueByAPR, DueByMAY, DueByJUN, DueByJUL, DueByAUG, DueBySEP, DueByOCT, DueByNOV, DueByDEC FROM LH_Mart.dbo.azure_franchiseetspa;
```

