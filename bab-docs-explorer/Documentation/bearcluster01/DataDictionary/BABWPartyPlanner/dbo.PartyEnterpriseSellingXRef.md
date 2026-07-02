# dbo.PartyEnterpriseSellingXRef

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyRequestID | int | 4 | 0 | YES |  |  |
| PartyID | int | 4 | 0 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 0 |  |  |  |
| OrderId | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.spLoadOrderIdForPartyESOrder](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spLoadOrderIdForPartyESOrder.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.spLoadOrderIdForPartyESOrder](../../StoredProcedures/BABWPartyPlanner/dbo.spLoadOrderIdForPartyESOrder.md)

