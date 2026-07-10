# dbo.tmp_gm1625Adjustments

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| discAmount | numeric | 9 | 0 |  |  |  |
| isGCCoupon | int | 4 | 0 |  |  |  |
| discReferenceNo | varchar | 80 | 1 |  |  |  |
| trans_line_sequence | numeric | 5 | 1 |  |  |  |
