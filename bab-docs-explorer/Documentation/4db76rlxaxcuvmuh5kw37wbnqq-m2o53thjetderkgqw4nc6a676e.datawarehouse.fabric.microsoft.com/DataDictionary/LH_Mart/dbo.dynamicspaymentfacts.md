# dbo.dynamicspaymentfacts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsPaymentFactsId | int | 4 | 1 |  |  |  |
| AmountCur | decimal | 9 | 1 |  |  |  |
| AmountMst | decimal | 9 | 1 |  |  |  |
| RetailAmountTendered | decimal | 9 | 1 |  |  |  |
| RetailCardTypeId | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| RetailTenderTypeId | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| AccountNum | varchar | 8000 | 1 |  |  |  |
| RetailCardNum | varchar | 8000 | 1 |  |  |  |
| ChangeLine | varchar | 8000 | 1 |  |  |  |
| PaymentAuthorization | varchar | 8000 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| CurrentSentDate | datetime2 | 8 | 1 |  |  |  |
| NegativeSentDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
