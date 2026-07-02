# dbo.Style

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCodeID | int | 4 | 0 | YES |  |  |
| StyleID | numeric | 9 | 0 |  |  |  |
| StyleCode | varchar | 20 | 0 |  |  |  |
| LongDesc | varchar | 120 | 1 |  |  |  |
| ShortDesc | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spDV_ActiveProducts](../../StoredProcedures/DBAUtility/dbo.spDV_ActiveProducts.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetProductByStyle](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetProductByStyle.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetProductForValidationByStyle](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetProductForValidationByStyle.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetStyleBySku](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetStyleBySku.md)
- [DBAUtility: dbo.spPFTGetOpenToByRollingCountsAndAttributes](../../StoredProcedures/DBAUtility/dbo.spPFTGetOpenToByRollingCountsAndAttributes.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetAllStyles](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetAllStyles.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetAllStylesData](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetAllStylesData.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetStyleCodeIdData](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetStyleCodeIdData.md)
- [BABWPartyPlanner_Restore: dbo.spMaintainStyle](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spMaintainStyle.md)
- [BABWPartyPlanner: dbo.sp_GetAllStyles](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetAllStyles.md)
- [BABWPartyPlanner: dbo.sp_GetAllStylesData](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetAllStylesData.md)
- [BABWPartyPlanner: dbo.sp_GetStyleCodeIdData](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetStyleCodeIdData.md)
- [BABWPartyPlanner: dbo.spMaintainStyle](../../StoredProcedures/BABWPartyPlanner/dbo.spMaintainStyle.md)

