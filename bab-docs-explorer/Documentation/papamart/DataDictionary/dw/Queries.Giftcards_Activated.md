# Queries.Giftcards_Activated

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 0 | YES |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| giftcard_no | varchar | 80 | 0 |  |  |  |
| DFLT_CRNCY_CODE | char | 3 | 1 |  |  |  |
