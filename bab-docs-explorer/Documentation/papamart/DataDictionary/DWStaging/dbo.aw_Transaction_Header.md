# dbo.aw_Transaction_Header

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| party_y_n | char | 1 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| batchNumber | int | 4 | 0 |  |  |  |
| transaction_type | varchar | 50 | 0 |  |  |  |
| currency_code | varchar | 3 | 1 |  |  |  |
| currency_key | int | 4 | 0 |  |  |  |
| cashier_key | int | 4 | 0 |  |  |  |
| party_master | bit | 1 | 0 |  |  |  |
| party_key | int | 4 | 1 |  |  |  |
