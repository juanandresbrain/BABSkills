# dbo.Survey_Register_Export_Line

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| unique_id | varchar | 30 | 1 |  |  |  |
| password | varchar | 30 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| sku | int | 4 | 1 |  |  |  |
| product_desc | varchar | 100 | 1 |  |  |  |
| department | varchar | 50 | 1 |  |  |  |
| department_code | varchar | 20 | 1 |  |  |  |
| subclass | varchar | 50 | 1 |  |  |  |
| subclass_code | varchar | 20 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_object_desc | varchar | 100 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| tender_group_key | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
