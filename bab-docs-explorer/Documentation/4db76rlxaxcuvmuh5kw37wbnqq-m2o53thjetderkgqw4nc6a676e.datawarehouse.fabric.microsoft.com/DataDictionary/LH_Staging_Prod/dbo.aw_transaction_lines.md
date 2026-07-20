# dbo.aw_transaction_lines

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| line_id | decimal | 5 | 1 |  |  |  |
| line_sequence | decimal | 5 | 1 |  |  |  |
| line_object_type | int | 4 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_action | int | 4 | 1 |  |  |  |
| gross_line_amount | decimal | 9 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| db_cr_none | int | 4 | 1 |  |  |  |
| reference_type | int | 4 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| voiding_reversal_flag | int | 4 | 1 |  |  |  |
