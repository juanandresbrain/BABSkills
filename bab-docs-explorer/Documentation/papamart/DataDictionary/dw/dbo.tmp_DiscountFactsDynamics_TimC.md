# dbo.tmp_DiscountFactsDynamics_TimC

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  |  |
| Line_Action | int | 4 | 0 |  |  |  |
| Line_Action_Description | nvarchar | 510 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| lift_amount | money | 8 | 0 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
