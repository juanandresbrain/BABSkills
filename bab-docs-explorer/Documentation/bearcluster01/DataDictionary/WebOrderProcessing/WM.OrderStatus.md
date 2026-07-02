# WM.OrderStatus

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderStatusId | int | 4 | 0 | YES |  |  |
| OrderId | int | 4 | 0 |  | YES |  |
| Status | varchar | 20 | 1 |  |  |  |
| StatusDate | datetime | 8 | 0 |  |  |  |
| CurrentStatus | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spStoreforceBopis](../../StoredProcedures/WebOrderProcessing/dbo.spStoreforceBopis.md)
- [WebOrderProcessing: WM.spGetESUpdateOrderStatus](../../StoredProcedures/WebOrderProcessing/WM.spGetESUpdateOrderStatus.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)
- [WebOrderProcessing: WM.spUKUpdateOrdersToShipped](../../StoredProcedures/WebOrderProcessing/WM.spUKUpdateOrdersToShipped.md)
- [WebOrderProcessing: WM.spUpdateWMOrderStatus_to_SalesAuditComplete](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMOrderStatus_to_SalesAuditComplete.md)
- [WebOrderProcessing: WM.spUpdateWMOrderStatusByOrderID](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMOrderStatusByOrderID.md)
- [WebOrderProcessing: WM.spWMPickticketXMLOnDemand](../../StoredProcedures/WebOrderProcessing/WM.spWMPickticketXMLOnDemand.md)

