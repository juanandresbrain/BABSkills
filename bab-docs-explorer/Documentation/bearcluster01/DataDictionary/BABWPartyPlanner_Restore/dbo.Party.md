# dbo.Party

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyID | int | 4 | 0 | YES |  |  |
| OccasionID | int | 4 | 1 |  | YES |  |
| TotalGuests | int | 4 | 1 |  |  |  |
| CustomerID | int | 4 | 1 |  | YES |  |
| EventID | int | 4 | 0 |  | YES |  |
| GOHAge | int | 4 | 1 |  |  |  |
| GOHFirstName | varchar | 50 | 1 |  |  |  |
| GOHGender | int | 4 | 1 |  |  |  |
| GuestAvgAge | int | 4 | 1 |  |  |  |
| PartyStateID | int | 4 | 1 |  | YES |  |
| DepositAmount | decimal | 5 | 1 |  |  |  |
| PackageID | int | 4 | 1 |  |  |  |
| POID | int | 4 | 1 |  |  |  |
| ThemeID | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.sp_InsertCommentFromPartyID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_InsertCommentFromPartyID.md)
- [BABWPartyPlanner_Restore: dbo.sp_InsertNewParty_V2](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_InsertNewParty_V2.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.sp_InsertCommentFromPartyID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_InsertCommentFromPartyID.md)
- [BABWPartyPlanner: dbo.sp_InsertNewParty_V2](../../StoredProcedures/BABWPartyPlanner/dbo.sp_InsertNewParty_V2.md)
- [BABWPartyPlanner: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md)

