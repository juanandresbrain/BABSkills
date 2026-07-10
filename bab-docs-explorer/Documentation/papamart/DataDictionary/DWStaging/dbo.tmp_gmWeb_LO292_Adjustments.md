# dbo.tmp_gmWeb_LO292_Adjustments

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
