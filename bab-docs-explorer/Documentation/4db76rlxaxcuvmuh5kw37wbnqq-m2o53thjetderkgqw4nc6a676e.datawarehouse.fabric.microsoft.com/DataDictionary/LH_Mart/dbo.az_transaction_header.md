# dbo.az_transaction_header

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | varchar | 200 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_no | varchar | 200 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| transaction_category | smallint | 2 | 1 |  |  |  |
| transaction_series | char | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| entry_date_time | datetime2 | 8 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| party_y_n | char | 4 | 1 |  |  |  |
| tender_total | decimal | 9 | 1 |  |  |  |
| batchNumber | int | 4 | 1 |  |  |  |
| transaction_type | varchar | 200 | 1 |  |  |  |
| currency_code | varchar | 12 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| cashier_key | int | 4 | 1 |  |  |  |
| party_master | int | 4 | 1 |  |  |  |
| party_key | int | 4 | 1 |  |  |  |
