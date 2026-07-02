# dbo.Package

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PackageID | int | 4 | 0 | YES |  |  |
| PackageName | varchar | -1 | 1 |  |  |  |
| Enabled | bit | 1 | 1 |  |  |  |
| IsTheme | bit | 1 | 1 |  |  |  |
| MinGuestSpend | numeric | 5 | 1 |  |  |  |
| PackageStartDate | datetime | 8 | 1 |  |  |  |
| PackageEndDate | datetime | 8 | 1 |  |  |  |
| ExecuteStartDate | datetime | 8 | 1 |  |  |  |
| ExecuteEndDate | datetime | 8 | 1 |  |  |  |
| PackageShortDesc | varchar | -1 | 1 |  |  |  |
| PackageLongDesc | varchar | -1 | 1 |  |  |  |
| EmailDescription | varchar | -1 | 1 |  |  |  |
| CountryID | int | 4 | 1 |  | YES |  |
| OrderBy | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)

