# dbo.Comment

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CommentID | int | 4 | 0 | YES |  |  |
| EventID | int | 4 | 1 |  | YES |  |
| CreatedDate | datetime | 8 | 1 |  |  |  |
| Comment | varchar | 512 | 1 |  |  |  |
| CreatedBy | varchar | 128 | 1 |  |  |  |
| LastUpdated | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.sp_SubmitBooking_V4](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_SubmitBooking_V4.md)
- [BABWPartyPlanner_Restore: dbo.sp_SubmitBooking_V5](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_SubmitBooking_V5.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByCustomer_SS20170725](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByCustomer_SS20170725.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventID](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventID.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByEventIDS](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByEventIDS.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.sp_SubmitBooking_V4](../../StoredProcedures/BABWPartyPlanner/dbo.sp_SubmitBooking_V4.md)
- [BABWPartyPlanner: dbo.sp_SubmitBooking_V5](../../StoredProcedures/BABWPartyPlanner/dbo.sp_SubmitBooking_V5.md)
- [BABWPartyPlanner: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner/dbo.sp_UpdateBooking_V3.md)

