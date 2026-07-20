# dbo.survey_register_export_line

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| unique_id | varchar | 8000 | 1 |  |  |  |
| password | varchar | 8000 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| register_num | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| sku | int | 4 | 1 |  |  |  |
| product_desc | varchar | 8000 | 1 |  |  |  |
| department | varchar | 8000 | 1 |  |  |  |
| department_code | varchar | 8000 | 1 |  |  |  |
| subclass | varchar | 8000 | 1 |  |  |  |
| subclass_code | varchar | 8000 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_object_desc | varchar | 8000 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| tender_group_key | int | 4 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
