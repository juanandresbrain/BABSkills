# dbo.franchisee_store_count_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| weekending_date_key | int | 4 | 1 |  |  |  |
| region_key | varchar | 8000 | 1 |  |  |  |
| store_count | int | 4 | 1 |  |  |  |
| src_extrct_dt | datetime2 | 8 | 1 |  |  |  |
| upd_dt | datetime2 | 8 | 1 |  |  |  |
| etl_log_id | int | 4 | 1 |  |  |  |
| etl_evnt_id | int | 4 | 1 |  |  |  |
