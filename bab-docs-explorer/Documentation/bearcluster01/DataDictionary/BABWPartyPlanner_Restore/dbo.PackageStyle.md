# dbo.PackageStyle

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PackageStyleID | int | 4 | 0 | YES |  |  |
| PackageID | int | 4 | 0 |  |  |  |
| StartDate | datetime | 8 | 0 |  |  |  |
| EndDate | datetime | 8 | 0 |  |  |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| CreatedDate | datetime | 8 | 0 |  |  |  |
| UpdatedBy | varchar | 255 | 1 |  |  |  |
| UpdatedOn | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_AddPackageStyleData](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_AddPackageStyleData.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetAllStyles](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetAllStyles.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetAllStylesData](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetAllStylesData.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetLargestPackageStyleID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetLargestPackageStyleID.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetNewStylesData](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetNewStylesData.md)
- [BABWPartyPlanner: dbo.sp_AddPackageStyleData](../../StoredProcedures/BABWPartyPlanner/dbo.sp_AddPackageStyleData.md)
- [BABWPartyPlanner: dbo.sp_GetAllStyles](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetAllStyles.md)
- [BABWPartyPlanner: dbo.sp_GetAllStylesData](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetAllStylesData.md)
- [BABWPartyPlanner: dbo.sp_GetLargestPackageStyleID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetLargestPackageStyleID.md)
- [BABWPartyPlanner: dbo.sp_GetNewStylesData](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetNewStylesData.md)

