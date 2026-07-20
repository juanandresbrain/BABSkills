# Style Report - Sat Week Ending

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 8c109854-14a2-40cb-80e2-bf6b5e083aec  
**Dataset ID:** 0d354f73-5a32-4d1d-9be1-e2681297b656  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/8c109854-14a2-40cb-80e2-bf6b5e083aec  
**Semantic Model:** [SM_AZAS_V2](../../SemanticModels/Enterprise Analytics Dev/SM_AZAS_V2.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Style Report - Sat Week Ending"]
    FranchiseeTSPA_WeekEndingDate(["FranchiseeTSPA.WeekEndingDate"]) --> REPORT
    FranchiseeTSPA_FranchiseeCountry(["FranchiseeTSPA.FranchiseeCountry"]) --> REPORT
    FranchiseeTSPA_Dept(["FranchiseeTSPA.Dept"]) --> REPORT
    Sum_FranchiseeTSPA_DptRnk_(["Sum(FranchiseeTSPA.DptRnk)"]) --> REPORT
    Sum_FranchiseeTSPA_CGrpRnk_(["Sum(FranchiseeTSPA.CGrpRnk)"]) --> REPORT
    Sum_FranchiseeTSPA_CGrpRnkPW_(["Sum(FranchiseeTSPA.CGrpRnkPW)"]) --> REPORT
    FranchiseeTSPA_KeyStory(["FranchiseeTSPA.KeyStory"]) --> REPORT
    FranchiseeTSPA_ConsGrp(["FranchiseeTSPA.ConsGrp"]) --> REPORT
    FranchiseeTSPA_Style_(["FranchiseeTSPA.Style#"]) --> REPORT
    FranchiseeTSPA_StyleDesc(["FranchiseeTSPA.StyleDesc"]) --> REPORT
    Sum_FranchiseeTSPA_NonPromoRtl_(["Sum(FranchiseeTSPA.NonPromoRtl)"]) --> REPORT
    Sum_FranchiseeTSPA_SlsULW_(["Sum(FranchiseeTSPA.SlsULW)"]) --> REPORT
    Sum_FranchiseeTSPA_SlsUPW_(["Sum(FranchiseeTSPA.SlsUPW)"]) --> REPORT
    Sum_FranchiseeTSPA_SlsU2PW_(["Sum(FranchiseeTSPA.SlsU2PW)"]) --> REPORT
    Sum_FranchiseeTSPA_SlsUYTD_(["Sum(FranchiseeTSPA.SlsUYTD)"]) --> REPORT
    Sum_FranchiseeTSPA_SlsR__(["Sum(FranchiseeTSPA.SlsR$)"]) --> REPORT
    Sum_FranchiseeTSPA_AUR_(["Sum(FranchiseeTSPA.AUR)"]) --> REPORT
    Sum_FranchiseeTSPA_Velcty_(["Sum(FranchiseeTSPA.Velcty)"]) --> REPORT
    Sum_FranchiseeTSPA_InStrST_(["Sum(FranchiseeTSPA.InStrST)"]) --> REPORT
    Sum_FranchiseeTSPA_WebStoresOnHand_(["Sum(FranchiseeTSPA.WebStoresOnHand)"]) --> REPORT
    Sum_FranchiseeTSPA_WarehouseOnHand_(["Sum(FranchiseeTSPA.WarehouseOnHand)"]) --> REPORT
    Sum_FranchiseeTSPA_TotalOnHand_(["Sum(FranchiseeTSPA.TotalOnHand)"]) --> REPORT
    Sum_FranchiseeTSPA_WeeksOfSupply_(["Sum(FranchiseeTSPA.WeeksOfSupply)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByJAN_(["Sum(FranchiseeTSPA.DueByJAN)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByFEB_(["Sum(FranchiseeTSPA.DueByFEB)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByMAR_(["Sum(FranchiseeTSPA.DueByMAR)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByAPR_(["Sum(FranchiseeTSPA.DueByAPR)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByMAY_(["Sum(FranchiseeTSPA.DueByMAY)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByJUN_(["Sum(FranchiseeTSPA.DueByJUN)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByJUL_(["Sum(FranchiseeTSPA.DueByJUL)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByAUG_(["Sum(FranchiseeTSPA.DueByAUG)"]) --> REPORT
    Sum_FranchiseeTSPA_DueBySEP_(["Sum(FranchiseeTSPA.DueBySEP)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByOCT_(["Sum(FranchiseeTSPA.DueByOCT)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByNOV_(["Sum(FranchiseeTSPA.DueByNOV)"]) --> REPORT
    Sum_FranchiseeTSPA_DueByDEC_(["Sum(FranchiseeTSPA.DueByDEC)"]) --> REPORT
    Sum_FranchiseeTSPA_YTDRnk_(["Sum(FranchiseeTSPA.YTDRnk)"]) --> REPORT
    Sum_FranchiseeTSPA_DptRnkPW_(["Sum(FranchiseeTSPA.DptRnkPW)"]) --> REPORT
    FranchiseeTSPA_MSTAT(["FranchiseeTSPA.MSTAT"]) --> REPORT
    Sum_FranchiseeTSPA_StoreOnHand_(["Sum(FranchiseeTSPA.StoreOnHand)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| FranchiseeTSPA.WeekEndingDate |
| FranchiseeTSPA.FranchiseeCountry |
| FranchiseeTSPA.Dept |
| Sum(FranchiseeTSPA.DptRnk) |
| Sum(FranchiseeTSPA.CGrpRnk) |
| Sum(FranchiseeTSPA.CGrpRnkPW) |
| FranchiseeTSPA.KeyStory |
| FranchiseeTSPA.ConsGrp |
| FranchiseeTSPA.Style# |
| FranchiseeTSPA.StyleDesc |
| Sum(FranchiseeTSPA.NonPromoRtl) |
| Sum(FranchiseeTSPA.SlsULW) |
| Sum(FranchiseeTSPA.SlsUPW) |
| Sum(FranchiseeTSPA.SlsU2PW) |
| Sum(FranchiseeTSPA.SlsUYTD) |
| Sum(FranchiseeTSPA.SlsR$) |
| Sum(FranchiseeTSPA.AUR) |
| Sum(FranchiseeTSPA.Velcty) |
| Sum(FranchiseeTSPA.InStrST) |
| Sum(FranchiseeTSPA.WebStoresOnHand) |
| Sum(FranchiseeTSPA.WarehouseOnHand) |
| Sum(FranchiseeTSPA.TotalOnHand) |
| Sum(FranchiseeTSPA.WeeksOfSupply) |
| Sum(FranchiseeTSPA.DueByJAN) |
| Sum(FranchiseeTSPA.DueByFEB) |
| Sum(FranchiseeTSPA.DueByMAR) |
| Sum(FranchiseeTSPA.DueByAPR) |
| Sum(FranchiseeTSPA.DueByMAY) |
| Sum(FranchiseeTSPA.DueByJUN) |
| Sum(FranchiseeTSPA.DueByJUL) |
| Sum(FranchiseeTSPA.DueByAUG) |
| Sum(FranchiseeTSPA.DueBySEP) |
| Sum(FranchiseeTSPA.DueByOCT) |
| Sum(FranchiseeTSPA.DueByNOV) |
| Sum(FranchiseeTSPA.DueByDEC) |
| Sum(FranchiseeTSPA.YTDRnk) |
| Sum(FranchiseeTSPA.DptRnkPW) |
| FranchiseeTSPA.MSTAT |
| Sum(FranchiseeTSPA.StoreOnHand) |

## Pages

| Page | Visuals |
|---|---|
| Page 1 | 2 |

## Visuals

### Page 1

| Visual | Type | Fields |
|---|---|---|
| 43f6de1b971d24b57827 | tableEx | FranchiseeTSPA.WeekEndingDate, FranchiseeTSPA.FranchiseeCountry, FranchiseeTSPA.Dept, Sum(FranchiseeTSPA.DptRnk), Sum(FranchiseeTSPA.CGrpRnk), Sum(FranchiseeTSPA.CGrpRnkPW), FranchiseeTSPA.KeyStory, FranchiseeTSPA.ConsGrp, FranchiseeTSPA.Style#, FranchiseeTSPA.StyleDesc, Sum(FranchiseeTSPA.NonPromoRtl), Sum(FranchiseeTSPA.SlsULW), Sum(FranchiseeTSPA.SlsUPW), Sum(FranchiseeTSPA.SlsU2PW), Sum(FranchiseeTSPA.SlsUYTD), Sum(FranchiseeTSPA.SlsR$), Sum(FranchiseeTSPA.AUR), Sum(FranchiseeTSPA.Velcty), Sum(FranchiseeTSPA.InStrST), Sum(FranchiseeTSPA.WebStoresOnHand), Sum(FranchiseeTSPA.WarehouseOnHand), Sum(FranchiseeTSPA.TotalOnHand), Sum(FranchiseeTSPA.WeeksOfSupply), Sum(FranchiseeTSPA.DueByJAN), Sum(FranchiseeTSPA.DueByFEB), Sum(FranchiseeTSPA.DueByMAR), Sum(FranchiseeTSPA.DueByAPR), Sum(FranchiseeTSPA.DueByMAY), Sum(FranchiseeTSPA.DueByJUN), Sum(FranchiseeTSPA.DueByJUL), Sum(FranchiseeTSPA.DueByAUG), Sum(FranchiseeTSPA.DueBySEP), Sum(FranchiseeTSPA.DueByOCT), Sum(FranchiseeTSPA.DueByNOV), Sum(FranchiseeTSPA.DueByDEC), Sum(FranchiseeTSPA.YTDRnk), Sum(FranchiseeTSPA.DptRnkPW), FranchiseeTSPA.MSTAT, Sum(FranchiseeTSPA.StoreOnHand) |
| 54abb6d164ec187494b7 | slicer | FranchiseeTSPA.FranchiseeCountry |
