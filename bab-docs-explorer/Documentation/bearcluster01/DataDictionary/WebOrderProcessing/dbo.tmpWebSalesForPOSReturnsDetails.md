# dbo.tmpWebSalesForPOSReturnsDetails

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| OrderItemID | int | 4 | 0 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| sku | varchar | 50 | 0 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |
| ItemLevelTax | numeric | 5 | 1 |  |  |  |
| Tender | numeric | 13 | 1 |  |  |  |
| currency_code | varchar | 3 | 1 |  |  |  |
| tfID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)

