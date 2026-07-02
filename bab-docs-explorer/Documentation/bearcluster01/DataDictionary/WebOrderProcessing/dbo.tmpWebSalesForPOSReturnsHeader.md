# dbo.tmpWebSalesForPOSReturnsHeader

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| currency_code | varchar | 3 | 1 |  |  |  |
| PaymentMethod | varchar | 50 | 1 |  |  |  |
| CardNum | varchar | 62 | 1 |  |  |  |
| Tax | decimal | 17 | 1 |  |  |  |
| SubTotal | money | 8 | 1 |  |  |  |
| Shipping | money | 8 | 1 |  |  |  |
| TotalCharges | money | 8 | 1 |  |  |  |
| TransactionAmount | money | 8 | 1 |  |  |  |
| PSPCode | varchar | 22 | 1 |  |  |  |
| tfID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)

