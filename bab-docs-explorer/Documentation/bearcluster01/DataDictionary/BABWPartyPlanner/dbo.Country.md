# dbo.Country

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CountryID | int | 4 | 0 | YES |  |  |
| CountryAbbr | varchar | 8 | 1 |  |  |  |
| CountryName | varchar | 128 | 1 |  |  |  |
| CurrencyCodeISO | varchar | 32 | 1 |  |  |  |
| CurrencySymbolISO | varchar | 1 | 1 |  |  |  |
| Enabled | bit | 1 | 1 |  |  |  |
| CountryKey | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)

