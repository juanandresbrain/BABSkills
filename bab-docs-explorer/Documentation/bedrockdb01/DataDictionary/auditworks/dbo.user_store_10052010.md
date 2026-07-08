# dbo.user_store_10052010

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| store_name | varchar | 30 | 0 |  |  |  |
| store_short_name | varchar | 12 | 0 |  |  |  |
| store_status_code | char | 1 | 0 |  |  |  |
| store_manager | varchar | 25 | 1 |  |  |  |
| selling_space | int | 4 | 1 |  |  |  |
| open_period | int | 4 | 1 |  |  |  |
| comp_period | int | 4 | 1 |  |  |  |
| closed_date | smalldatetime | 4 | 1 |  |  |  |
| selling_nonselling_flag | tinyint | 1 | 0 |  |  |  |
| division_code | smallint | 2 | 0 |  |  |  |
| region_code | varchar | 8 | 0 |  |  |  |
| district_code | varchar | 8 | 0 |  |  |  |
| phone_no | varchar | 20 | 1 |  |  |  |
| time_stamp | timestamp | 8 | 1 |  |  |  |
| location_id | numeric | 5 | 1 |  |  |  |
| comp_date | smalldatetime | 4 | 1 |  |  |  |
| open_date | smalldatetime | 4 | 1 |  |  |  |
| settlement_billing_name | varchar | 20 | 1 |  |  |  |
| country_code | varchar | 3 | 1 |  |  |  |
| city | varchar | 20 | 1 |  |  |  |
| state_code | varchar | 2 | 1 |  |  |  |
| zip_code | varchar | 20 | 1 |  |  |  |
