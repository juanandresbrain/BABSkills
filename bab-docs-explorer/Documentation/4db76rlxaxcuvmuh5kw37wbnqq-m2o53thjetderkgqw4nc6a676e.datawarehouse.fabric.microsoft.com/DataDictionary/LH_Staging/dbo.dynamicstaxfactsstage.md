# dbo.dynamicstaxfactsstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Amount | decimal | 9 | 1 |  |  |  |
| LineNum | int | 4 | 1 |  |  |  |
| SaleLineNum | int | 4 | 1 |  |  |  |
| TaxCode | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| TaxRate | decimal | 9 | 1 |  |  |  |
