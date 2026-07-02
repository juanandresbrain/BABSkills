# dbo.Event

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | int | 4 | 0 | YES |  |  |
| EventStart | datetime | 8 | 1 |  |  |  |
| EventEnd | datetime | 8 | 1 |  |  |  |
| EventType | int | 4 | 1 |  |  |  |
| CreatedDate | datetime | 8 | 1 |  |  |  |
| CreatedBy | varchar | 128 | 1 |  |  |  |
| LastUpdated | datetime | 8 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  | YES |  |
| Active | bit | 1 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ReportServerBIRPT02: dbo.AddEvent](../../StoredProcedures/ReportServerBIRPT02/dbo.AddEvent.md)
- [ReportServerBIRPT02: dbo.CleanEventRecords](../../StoredProcedures/ReportServerBIRPT02/dbo.CleanEventRecords.md)
- [ReportServerBIRPT02: dbo.CreateCacheUpdateNotifications](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateCacheUpdateNotifications.md)
- [ReportServerBIRPT02: dbo.CreateSnapShotNotifications](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateSnapShotNotifications.md)
- [ReportServerBIRPT02: dbo.CreateTimeBasedSubscriptionNotification](../../StoredProcedures/ReportServerBIRPT02/dbo.CreateTimeBasedSubscriptionNotification.md)
- [ReportServerBIRPT02: dbo.DeleteEvent](../../StoredProcedures/ReportServerBIRPT02/dbo.DeleteEvent.md)
- [ReportServerBIRPT02: dbo.PollEventsForRSProcess](../../StoredProcedures/ReportServerBIRPT02/dbo.PollEventsForRSProcess.md)
- [ReportServerBIRPT02: dbo.TakeEventFromQueue](../../StoredProcedures/ReportServerBIRPT02/dbo.TakeEventFromQueue.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedDatesAndTimesByStore_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedDatesAndTimesByStore_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_GSPartyBookingsReportDaily](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_GSPartyBookingsReportDaily.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md)
- [BABWPartyPlanner_Restore: dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md)
- [BABWPartyPlanner: dbo.sp_GetBookedDatesAndTimesByStore_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedDatesAndTimesByStore_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
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

