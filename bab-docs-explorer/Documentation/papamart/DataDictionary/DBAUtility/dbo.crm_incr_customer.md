# dbo.crm_incr_customer

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_key | int | 4 | 1 |  |  |  |
| household_key | int | 4 | 1 |  |  |  |
| address_key | int | 4 | 1 |  |  |  |
| seq_no | int | 4 | 1 |  |  |  |
| source | varchar | 20 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| crm_upload_date | datetime | 8 | 1 |  |  |  |
