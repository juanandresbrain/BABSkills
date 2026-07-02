# WM.ItemStatus_Archive

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemStatusId | int | 4 | 0 |  |  |  |
| OrderItemID | int | 4 | 0 |  |  |  |
| Status | varchar | 20 | 1 |  |  |  |
| StatusDate | datetime | 8 | 0 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |
| OrderID | int | 4 | 0 |  |  |  |
| OrderTransactionIdentifier | int | 4 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)

