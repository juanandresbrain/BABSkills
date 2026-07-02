# WM.ShippingDiscounts

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingDiscountID | int | 4 | 0 | YES |  |  |
| OrderId | int | 4 | 0 |  | YES |  |
| PromoCode | varchar | 40 | 1 |  |  |  |
| DiscountAmount | money | 8 | 1 |  |  |  |
| DiscountName | varchar | 50 | 1 |  |  |  |
| OrderNum | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V3_1.md)

