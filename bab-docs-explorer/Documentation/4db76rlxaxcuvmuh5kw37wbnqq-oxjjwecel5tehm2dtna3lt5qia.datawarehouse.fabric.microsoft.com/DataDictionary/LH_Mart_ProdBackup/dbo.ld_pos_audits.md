# dbo.ld_pos_audits

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 1 |  |  |  |
| modified_date | datetime2 | 8 | 1 |  |  |  |
| entry_date | datetime2 | 8 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| dm_deleted_y_n | varchar | 8000 | 1 |  |  |  |
| dm_deleted_date | datetime2 | 8 | 1 |  |  |  |
| seqno | int | 4 | 1 |  |  |  |
