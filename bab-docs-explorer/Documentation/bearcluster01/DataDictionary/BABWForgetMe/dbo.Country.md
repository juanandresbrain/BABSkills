# dbo.Country

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CountryID | int | 4 | 0 | YES |  |  |
| Country | nvarchar | 100 | 0 |  |  |  |
| CountryAbbr | nvarchar | 20 | 1 |  |  |  |
| SFCCCountryID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)

