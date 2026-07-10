# dbo.DiscountFactsDynamics_TestTC1

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  |  |
| transaction_id | decimal | 9 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| coupon_key | int | 4 | 0 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| uid | int | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| UPDT_DT | datetime | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 0 |  |  |  |
| isExpired | bit | 1 | 0 |  |  |  |
| lift_amount | money | 8 | 0 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
