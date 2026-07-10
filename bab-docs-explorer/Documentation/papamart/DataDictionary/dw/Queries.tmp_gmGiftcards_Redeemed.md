# Queries.tmp_gmGiftcards_Redeemed

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| db_cr_none | smallint | 2 | 0 |  |  |  |
| DFLT_CRNCY_CODE | nchar | 6 | 1 |  |  |  |
