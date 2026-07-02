# WM.OMSTransactionDetails

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TansactionDetailID | int | 4 | 0 | YES |  |  |
| TransactionID | int | 4 | 0 |  | YES |  |
| ShipmentNumber | int | 4 | 1 |  |  |  |
| OrderTransactionIdentifier | int | 4 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 0 |  |  |  |
| SubTotal | money | 8 | 0 |  |  |  |
| Shipping | money | 8 | 0 |  |  |  |
| ProcessingFee | money | 8 | 0 |  |  |  |
| Tax | decimal | 5 | 1 |  |  |  |
| TotalCharges | money | 8 | 0 |  |  |  |
| PaymentTransactionType | varchar | 50 | 1 |  |  |  |
| PaymentType | varchar | 50 | 1 |  |  |  |
| TransactionAmount | money | 8 | 0 |  |  |  |
| OrderDiscount | money | 8 | 0 |  |  |  |
| ItemDiscount | money | 8 | 0 |  |  |  |
| InvoiceAmount | money | 8 | 0 |  |  |  |
| InvoiceBillTo | varchar | 50 | 1 |  |  |  |
| InvoiceNumber | varchar | 50 | 1 |  |  |  |
| InvoiceDate | datetime | 8 | 1 |  |  |  |
| Processor | varchar | 255 | 1 |  |  |  |
| CurrencyMultiplier | int | 4 | 0 |  |  |  |
| OmsTransactionType | varchar | 255 | 1 |  |  |  |
| PaymentGeneric1 | varchar | 50 | 1 |  |  |  |
| PaymentGeneric2 | varchar | 50 | 1 |  |  |  |
| PaymentGeneric3 | varchar | 50 | 1 |  |  |  |
| PaymentGeneric4 | varchar | 50 | 1 |  |  |  |
| PaymentGeneric5 | varchar | 50 | 1 |  |  |  |
| TransactionGeneric1 | varchar | 50 | 1 |  |  |  |
| TransactionGeneric2 | varchar | 50 | 1 |  |  |  |
| TransactionGeneric3 | varchar | 50 | 1 |  |  |  |
| TransactionGeneric4 | varchar | 50 | 1 |  |  |  |
| TransactionGeneric5 | varchar | 50 | 1 |  |  |  |
| isSAProcessed | bit | 1 | 1 |  |  |  |
| BillToFName | varchar | 50 | 1 |  |  |  |
| BillToLName | varchar | 50 | 1 |  |  |  |
| BillToAddress1 | varchar | 100 | 1 |  |  |  |
| BillToAddress2 | varchar | 100 | 1 |  |  |  |
| BillToCity | varchar | 50 | 1 |  |  |  |
| BillToState | varchar | 50 | 1 |  |  |  |
| BillToPostalCode | varchar | 20 | 1 |  |  |  |
| BillToCountry | varchar | 30 | 1 |  |  |  |
| BillToEmail | varchar | 100 | 1 |  |  |  |
| BillToPhone | varchar | 20 | 1 |  |  |  |
| ShipToFName | varchar | 50 | 1 |  |  |  |
| ShipToLName | varchar | 50 | 1 |  |  |  |
| ShipToAddress1 | varchar | 100 | 1 |  |  |  |
| ShipToAddress2 | varchar | 100 | 1 |  |  |  |
| ShipToCity | varchar | 50 | 1 |  |  |  |
| ShipToState | varchar | 50 | 1 |  |  |  |
| ShipToPostalCode | varchar | 20 | 1 |  |  |  |
| ShipToCountry | varchar | 30 | 1 |  |  |  |
| ShipToEmail | varchar | 100 | 1 |  |  |  |
| ShipToPhone | varchar | 20 | 1 |  |  |  |
| OrderCustom1 | varchar | 255 | 1 |  |  |  |
| OrderCustom2 | varchar | 255 | 1 |  |  |  |
| OrderCustom3 | varchar | 255 | 1 |  |  |  |
| OrderCustom4 | varchar | 255 | 1 |  |  |  |
| OrderCustom5 | varchar | 255 | 1 |  |  |  |
| isDecline | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics0_BuildTargetTransactionsTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics0_BuildTargetTransactionsTable.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V3.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V3_1.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)
- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete.md)
- [WebOrderProcessing: WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMItemStatus_to_SalesAuditComplete_BJB20200715.md)

