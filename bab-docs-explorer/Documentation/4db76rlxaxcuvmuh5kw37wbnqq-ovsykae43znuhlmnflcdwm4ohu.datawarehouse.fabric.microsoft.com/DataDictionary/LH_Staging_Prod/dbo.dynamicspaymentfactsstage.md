# dbo.dynamicspaymentfactsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
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
