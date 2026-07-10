# dbo.tmpDwTaxTotalsByTransaction

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| tender_code | varchar | 5 | 1 |  |  |  |
| tender_desc | varchar | 50 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 5 | 1 |  |  |  |
| SumTaxAmount | numeric | 17 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
