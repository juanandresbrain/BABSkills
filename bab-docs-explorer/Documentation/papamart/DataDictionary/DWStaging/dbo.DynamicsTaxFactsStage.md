# dbo.DynamicsTaxFactsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Amount | decimal | 9 | 1 |  |  |  |
| LineNum | int | 4 | 1 |  |  |  |
| SaleLineNum | int | 4 | 1 |  |  |  |
| TaxCode | varchar | 50 | 1 |  |  |  |
| RetailTerminalId | varchar | 10 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8 | 1 |  |  |  |
| BABIntRetailProcessed | varchar | 10 | 1 |  |  |  |
| Entity | varchar | 10 | 1 |  |  |  |
| RetailReceiptId | varchar | 18 | 1 |  |  |  |
| TaxRate | decimal | 9 | 1 |  |  |  |
