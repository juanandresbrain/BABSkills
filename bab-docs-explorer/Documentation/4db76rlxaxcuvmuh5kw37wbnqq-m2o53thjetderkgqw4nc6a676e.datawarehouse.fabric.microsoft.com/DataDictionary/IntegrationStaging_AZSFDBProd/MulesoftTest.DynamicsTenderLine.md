# MulesoftTest.DynamicsTenderLine

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | -1 | 1 |  |  |  |
| AmountCur | decimal | 9 | 1 |  |  |  |
| AmountMst | decimal | 9 | 1 |  |  |  |
| RetailAmountTendered | decimal | 9 | 1 |  |  |  |
| NativePaymentMethod | varchar | -1 | 1 |  |  |  |
| NativeCardType | varchar | -1 | 1 |  |  |  |
| RetailCardTypeId | varchar | -1 | 0 |  |  |  |
| RetailReceiptId | varchar | -1 | 1 |  |  |  |
| LineNum | bigint | 8 | 1 |  |  |  |
| RetailTransactionId | varchar | -1 | 1 |  |  |  |
| RetailTenderTypeId | varchar | -1 | 0 |  |  |  |
| RetailTerminalId | varchar | -1 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | -1 | 0 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| AccountNum | int | 4 | 1 |  |  |  |
| RetailCardNum | int | 4 | 1 |  |  |  |
| ChangeLine | varchar | -1 | 0 |  |  |  |
| PaymentAuthorization | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | -1 | 1 |  |  |  |
| Entity | varchar | -1 | 1 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | -1 | 1 |  |  |  |
| InventLocationId | varchar | -1 | 1 |  |  |  |
| BatchID | varchar | -1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1997250170 | bigint | 8 | 0 |  |  |  |
