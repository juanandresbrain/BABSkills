# dbo.azure_pos_compare_jump_mind_stage_to_sales_audit

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | varchar | 8000 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| trans_nbr | bigint | 8 | 1 |  |  |  |
| total | decimal | 9 | 1 |  |  |  |
| trans_type | varchar | 8000 | 1 |  |  |  |
| trans_status | varchar | 8000 | 1 |  |  |  |
| loyalty_card_number | varchar | 8000 | 1 |  |  |  |
| customer_id | varchar | 8000 | 1 |  |  |  |
| Employee | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| entry_date_time | datetime2 | 8 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| tender_total | decimal | 9 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| EntryDate | date | 3 | 1 |  |  |  |
| customer_no | decimal | 13 | 1 |  |  |  |
| LTFSales | decimal | 9 | 1 |  |  |  |
| LTFPoints | decimal | 9 | 1 |  |  |  |
