# WM.tmpOrderOrderTransactionIdentifier

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| PickupStore | varchar | 4 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
| OrderTransactionIdentifier | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V3_2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderBillTo_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderBillTo_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_2_BJB20250906](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_2_BJB20250906.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V3_2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShipTo_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShipTo_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes_V3_1.md)
- [WebOrderProcessing: WM.spTruncateAndReloadtmpOrderOrderTransactionIdentifier](../../StoredProcedures/WebOrderProcessing/WM.spTruncateAndReloadtmpOrderOrderTransactionIdentifier.md)

