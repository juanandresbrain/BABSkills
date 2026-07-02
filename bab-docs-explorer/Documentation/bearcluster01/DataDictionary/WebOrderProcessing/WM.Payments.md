# WM.Payments

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PaymentID | int | 4 | 0 | YES |  |  |
| TransactionID | int | 4 | 0 |  | YES |  |
| PaymentMethod | varchar | 20 | 1 |  |  |  |
| PaymentAmount | money | 8 | 1 |  |  |  |
| PaymentAuthCode | varchar | 22 | 1 |  |  |  |
| PaymentNum | varchar | 22 | 1 |  |  |  |
| CardType | varchar | 20 | 1 |  |  |  |
| CreditCardNumber | varchar | 20 | 1 |  |  |  |
| PayerID | varchar | 20 | 1 |  |  |  |
| GiftCardNumber | varchar | 20 | 1 |  |  |  |
| VoucherNumber | varchar | 20 | 1 |  |  |  |
| TransactionNum | varchar | 22 | 1 |  |  |  |
| GuestSatisfactionRefund | money | 8 | 1 |  |  |  |
| ExpirationMonth | varchar | 2 | 1 |  |  |  |
| ExpirationYear | varchar | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)
- [WebOrderProcessing: WM.spUpdateChannelAdvisorSets](../../StoredProcedures/WebOrderProcessing/WM.spUpdateChannelAdvisorSets.md)

