# dbo.tmp_discountfactsdynamics_timc

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 8000 | 1 |  |  |  |
| Line_Action | int | 4 | 1 |  |  |  |
| Line_Action_Description | varchar | 8000 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| lift_amount | decimal | 9 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
