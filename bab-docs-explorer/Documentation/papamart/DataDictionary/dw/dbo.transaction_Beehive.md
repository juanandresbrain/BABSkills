# dbo.transaction_Beehive

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | datetime | 8 | 1 |  |  |  |
| Store_no | int | 4 | 1 |  |  |  |
| Register_no | int | 4 | 1 |  |  |  |
| Transaction_ID | int | 4 | 1 |  |  |  |
| Line_id | int | 4 | 1 |  |  |  |
| Line_Sequence | int | 4 | 1 |  |  |  |
| Cashier_no | varchar | 8 | 1 |  |  |  |
| Gross_line_Amount | money | 8 | 1 |  |  |  |
| Pos_Discount_amount | money | 8 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_object_type | int | 4 | 1 |  |  |  |
| line_object_description | varchar | 255 | 1 |  |  |  |
| Pos_discount_type | varchar | 10 | 1 |  |  |  |
| Reference_no | varchar | 20 | 1 |  |  |  |
| Line_action | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| transaction_category | int | 4 | 1 |  |  |  |
| BSR | char | 1 | 1 |  |  |  |
