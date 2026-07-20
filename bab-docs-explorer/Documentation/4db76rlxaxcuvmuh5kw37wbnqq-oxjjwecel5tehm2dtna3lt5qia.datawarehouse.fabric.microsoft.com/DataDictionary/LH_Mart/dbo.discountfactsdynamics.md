# dbo.discountfactsdynamics

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| reference_no | varchar | 8000 | 1 |  |  |  |
| process_name | varchar | 8000 | 1 |  |  |  |
| process_date | datetime2 | 8 | 1 |  |  |  |
| uid | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| lift_amount | decimal | 9 | 1 |  |  |  |
| line_action_key | int | 4 | 1 |  |  |  |
