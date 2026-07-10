# dbo.tmpBakDynamicsPaymentComparison

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PaymentStageLineNum | bigint | 8 | 1 |  |  |  |
| PaymentStageRetailTenderTypeId | varchar | 50 | 1 |  |  |  |
| PaymentStageAmountCur | numeric | 9 | 1 |  |  |  |
| AmountCur | numeric | 9 | 1 |  |  |  |
| AmountMst | numeric | 9 | 1 |  |  |  |
| RetailAmountTendered | numeric | 9 | 1 |  |  |  |
| RetailCardTypeId | varchar | 10 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| RetailTenderTypeId | varchar | 50 | 1 |  |  |  |
| RetailTerminalId | varchar | 10 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| AccountNum | varchar | 20 | 1 |  |  |  |
| RetailCardNum | varchar | 16 | 1 |  |  |  |
| ChangeLine | varchar | 4 | 1 |  |  |  |
| PaymentAuthorization | varchar | 10 | 1 |  |  |  |
| CurrencyCode | varchar | 3 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 10 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
