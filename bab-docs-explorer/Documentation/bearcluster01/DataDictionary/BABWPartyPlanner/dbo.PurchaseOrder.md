# dbo.PurchaseOrder

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POID | int | 4 | 0 |  |  |  |
| PONumber | varchar | 64 | 0 |  |  |  |
| CustomerID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_UpdateBooking_V3.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.sp_UpdateBooking_V3](../../StoredProcedures/BABWPartyPlanner/dbo.sp_UpdateBooking_V3.md)

