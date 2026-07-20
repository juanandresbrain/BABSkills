# dbo.mulesofttest_dynamicstaxline

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| Amount | decimal | 9 | 1 |  |  |  |
| LineNum | varchar | 8000 | 1 |  |  |  |
| TaxCode | varchar | 8000 | 0 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1981250113 | bigint | 8 | 0 |  |  |  |
