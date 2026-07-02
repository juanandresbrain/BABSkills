# dbo.dynamicstenderlinestage

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 136 | 1 |  |  |  |
| AmountCur | money | 8 | 1 |  |  |  |
| AmountMst | money | 8 | 1 |  |  |  |
| RetailAmountTendered | money | 8 | 1 |  |  |  |
| NativePaymentMethod | varchar | 20 | 1 |  |  |  |
| NativeCardType | varchar | 20 | 1 |  |  |  |
| RetailCardTypeId | varchar | 12 | 0 |  |  |  |
| RetailReceiptId | varchar | 50 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| RetailTransactionId | varchar | 138 | 1 |  |  |  |
| RetailTenderTypeId | varchar | 12 | 0 |  |  |  |
| RetailTerminalId | varchar | 53 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 14 | 0 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| AccountNum | int | 4 | 1 |  |  |  |
| RetailCardNum | int | 4 | 1 |  |  |  |
| ChangeLine | varchar | 2 | 0 |  |  |  |
| PaymentAuthorization | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 3 | 1 |  |  |  |
| Entity | varchar | 4 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| CreateTime | datetime | 8 | 1 |  |  |  |
| Barcode | varchar | 50 | 1 |  |  |  |
| InventLocationId | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)

