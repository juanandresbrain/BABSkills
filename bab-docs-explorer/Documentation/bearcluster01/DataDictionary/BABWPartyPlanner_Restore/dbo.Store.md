# dbo.Store

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 0 | YES |  |  |
| MinutesBetweenParties | int | 4 | 1 |  |  |  |
| BookingParties | bit | 1 | 1 |  |  |  |
| WebMessage | varchar | 8000 | 1 |  |  |  |
| BSRMessage | varchar | 8000 | 1 |  |  |  |
| ParentStore | int | 4 | 1 |  |  |  |
| CancellationHours | int | 4 | 1 |  |  |  |
| ModificationDays | int | 4 | 1 |  |  |  |
| MinGuests | int | 4 | 1 |  |  |  |
| MaxGuests | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| DefaultStartOffset | int | 4 | 1 |  |  |  |
| DefaultEndOffset | int | 4 | 1 |  |  |  |
| StoreGroupID | int | 4 | 1 |  | YES |  |
| CountryID | int | 4 | 1 |  |  |  |
| CanBookOnline | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedDatesAndTimesByStore_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedDatesAndTimesByStore_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md)
- [BABWPartyPlanner: dbo.sp_GetBookedDatesAndTimesByStore_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedDatesAndTimesByStore_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetPartyChoicesByStore_V2](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetPartyChoicesByStore_V2.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md)
- [BABWPartyPlanner: dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md)
- [BABWPartyPlanner: dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419](../../StoredProcedures/BABWPartyPlanner/dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md)

