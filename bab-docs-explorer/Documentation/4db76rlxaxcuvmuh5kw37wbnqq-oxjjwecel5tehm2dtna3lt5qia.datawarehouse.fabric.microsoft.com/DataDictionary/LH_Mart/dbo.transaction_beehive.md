# dbo.transaction_beehive

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| Store_no | int | 4 | 1 |  |  |  |
| Register_no | int | 4 | 1 |  |  |  |
| Transaction_ID | int | 4 | 1 |  |  |  |
| Line_id | int | 4 | 1 |  |  |  |
| Line_Sequence | int | 4 | 1 |  |  |  |
| Cashier_no | varchar | 8000 | 1 |  |  |  |
| Gross_line_Amount | decimal | 9 | 1 |  |  |  |
| Pos_Discount_amount | decimal | 9 | 1 |  |  |  |
| entry_date_time | datetime2 | 8 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_object_type | int | 4 | 1 |  |  |  |
| line_object_description | varchar | 8000 | 1 |  |  |  |
| Pos_discount_type | varchar | 8000 | 1 |  |  |  |
| Reference_no | varchar | 8000 | 1 |  |  |  |
| Line_action | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| transaction_category | int | 4 | 1 |  |  |  |
| BSR | varchar | 8000 | 1 |  |  |  |
