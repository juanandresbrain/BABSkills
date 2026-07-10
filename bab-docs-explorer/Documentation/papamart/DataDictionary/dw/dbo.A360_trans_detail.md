# dbo.A360_trans_detail

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionLineItemID | varchar | 50 | 0 |  |  |  |
| purchaseDate | datetime | 8 | 1 |  |  |  |
| style_code | varchar | 50 | 1 |  |  |  |
| purchaseRevene | numeric | 17 | 1 |  |  |  |
| unit_disc_amount | numeric | 17 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| transaction_id | varchar | 50 | 1 |  |  |  |
| perUnitRevenue | numeric | 17 | 1 |  |  |  |
