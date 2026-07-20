# dbo.dynamicstaxfacts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsTaxFactsId | int | 4 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| LineNum | int | 4 | 1 |  |  |  |
| TaxCode | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| IsNegatedCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| CurrentSentDate | datetime2 | 8 | 1 |  |  |  |
| NegativeSentDate | datetime2 | 8 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
