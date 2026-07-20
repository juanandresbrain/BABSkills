# dbo.aw_transaction_header

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | int | 4 | 1 |  |  |  |
| transaction_series | varchar | 8000 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| entry_date_time | datetime2 | 8 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| party_y_n | varchar | 8000 | 1 |  |  |  |
| tender_total | decimal | 9 | 1 |  |  |  |
| batchNumber | int | 4 | 1 |  |  |  |
| transaction_type | varchar | 8000 | 1 |  |  |  |
| currency_code | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| cashier_key | int | 4 | 1 |  |  |  |
| party_master | bit | 1 | 1 |  |  |  |
| party_key | int | 4 | 1 |  |  |  |
