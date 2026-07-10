# dbo.A360_trans_header

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| country | varchar | 50 | 1 |  |  |  |
| customerNumber | varchar | 50 | 1 |  |  |  |
| purchaseChannel | varchar | 50 | 1 |  |  |  |
| purchaseDate | datetime | 8 | 1 |  |  |  |
| purchaseStoreNumber | varchar | 50 | 1 |  |  |  |
| purchaseRevenue | numeric | 17 | 1 |  |  |  |
| purchaseUnitCount | numeric | 17 | 1 |  |  |  |
| transaction_id | varchar | 50 | 0 |  |  |  |
