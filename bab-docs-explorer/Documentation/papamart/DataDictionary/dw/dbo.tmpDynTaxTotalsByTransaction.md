# dbo.tmpDynTaxTotalsByTransaction

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| SumTaxAmount | numeric | 17 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| transaction_id | varchar | 18 | 1 |  |  |  |
