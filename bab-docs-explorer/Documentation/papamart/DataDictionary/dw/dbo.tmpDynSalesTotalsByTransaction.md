# dbo.tmpDynSalesTotalsByTransaction

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| SumDynUnitGrossAmount | numeric | 17 | 1 |  |  |  |
| SumDynUnitDiscAmt | numeric | 17 | 1 |  |  |  |
| SumDynSalesTotal | numeric | 17 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
