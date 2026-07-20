# dbo.mulesoft_dynamicstenderlineoms

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| AmountCur | decimal | 9 | 1 |  |  |  |
| AmountMst | decimal | 9 | 1 |  |  |  |
| RetailAmountTendered | decimal | 9 | 1 |  |  |  |
| NativePaymentMethod | varchar | 8000 | 1 |  |  |  |
| NativeCardType | varchar | 8000 | 1 |  |  |  |
| RetailCardTypeId | varchar | 8000 | 0 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| RetailTenderTypeId | varchar | 8000 | 0 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 0 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| AccountNum | int | 4 | 1 |  |  |  |
| RetailCardNum | int | 4 | 1 |  |  |  |
| ChangeLine | varchar | 8000 | 0 |  |  |  |
| PaymentAuthorization | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1766297352 | bigint | 8 | 0 |  |  |  |
