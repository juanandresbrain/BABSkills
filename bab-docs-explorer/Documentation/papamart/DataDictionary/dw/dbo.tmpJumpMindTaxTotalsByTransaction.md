# dbo.tmpJumpMindTaxTotalsByTransaction

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 128 | 1 |  |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| JumpMindHeaderTaxTotal | numeric | 17 | 1 |  |  |  |
