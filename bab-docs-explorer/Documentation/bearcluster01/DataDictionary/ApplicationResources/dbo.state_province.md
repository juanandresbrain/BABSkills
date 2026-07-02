# dbo.state_province

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| st_prvnc_id | int | 4 | 0 | YES |  |  |
| nm_abbrv | varchar | 10 | 0 |  |  |  |
| nm_full | varchar | 255 | 0 |  |  |  |
| cntry_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.sp_GetJumpMindTaxState](../../StoredProcedures/ApplicationResources/dbo.sp_GetJumpMindTaxState.md)

