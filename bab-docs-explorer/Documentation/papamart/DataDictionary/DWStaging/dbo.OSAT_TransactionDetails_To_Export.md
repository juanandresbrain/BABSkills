# dbo.OSAT_TransactionDetails_To_Export

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 0 |  |  |  |
| unique_id | varchar | 30 | 0 |  |  |  |
| password | varchar | 30 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| time_key | int | 4 | 0 |  |  |  |
| register_num | int | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| sku | bigint | 8 | 1 |  |  |  |
| product_desc | varchar | 40 | 1 |  |  |  |
| department | varchar | 20 | 1 |  |  |  |
| department_code | varchar | 20 | 1 |  |  |  |
| subclass | varchar | 20 | 1 |  |  |  |
| subclass_code | varchar | 20 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| tender_group_key | int | 4 | 0 |  |  |  |
| product_key | int | 4 | 0 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  |  |
