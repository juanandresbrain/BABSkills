# dbo.DynamicsPaymentFacts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsPaymentFactsId | int | 4 | 0 | YES |  |  |
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
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CurrentSentDate | datetime | 8 | 1 |  |  |  |
| NegativeSentDate | datetime | 8 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
