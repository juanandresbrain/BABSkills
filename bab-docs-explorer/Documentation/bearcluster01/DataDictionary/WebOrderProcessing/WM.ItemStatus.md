# WM.ItemStatus

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemStatusId | int | 4 | 0 | YES |  |  |
| OrderItemID | int | 4 | 0 |  | YES |  |
| Status | varchar | 20 | 1 |  |  |  |
| StatusDate | datetime | 8 | 0 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |
| OrderID | int | 4 | 0 |  | YES |  |
| OrderTransactionIdentifier | int | 4 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3_1.md)
- [WebOrderProcessing: WM.spUpdateChannelAdvisorSets](../../StoredProcedures/WebOrderProcessing/WM.spUpdateChannelAdvisorSets.md)
- [WebOrderProcessing: WM.spWMPickticketXMLOnDemand](../../StoredProcedures/WebOrderProcessing/WM.spWMPickticketXMLOnDemand.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)

