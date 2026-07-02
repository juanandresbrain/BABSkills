# WM.ItemDiscounts

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DiscountID | int | 4 | 0 | YES |  |  |
| OrderItemID | int | 4 | 0 |  | YES |  |
| PromoCode | varchar | 40 | 1 |  |  |  |
| DiscountAmount | money | 8 | 1 |  |  |  |
| IsOrderDiscount | bit | 1 | 1 |  |  |  |
| DiscountName | varchar | 50 | 1 |  |  |  |
| OrderID | int | 4 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V2.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3_1.md)

