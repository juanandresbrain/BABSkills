# dbo.Customer

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerID | int | 4 | 0 | YES |  |  |
| FirstName | varchar | 64 | 1 |  |  |  |
| LastName | varchar | 64 | 1 |  |  |  |
| PrimaryPhone | varchar | 32 | 1 |  |  |  |
| SecondaryPhone | varchar | 32 | 1 |  |  |  |
| EmailAddress | varchar | 128 | 1 |  |  |  |
| CustomerNumber | varchar | 32 | 1 |  |  |  |
| Address1 | varchar | 128 | 1 |  |  |  |
| Address2 | varchar | 128 | 1 |  |  |  |
| City | varchar | 128 | 1 |  |  |  |
| State | varchar | 32 | 1 |  |  |  |
| Zipcode | varchar | 13 | 1 |  |  |  |
| Country | varchar | 64 | 1 |  |  |  |
| Organization | varchar | 64 | 1 |  |  |  |
| TaxId | varchar | 64 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)

