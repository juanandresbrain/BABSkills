# dbo.franchisee_store_count_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| weekending_date_key | int | 4 | 0 |  |  |  |
| region_key | varchar | 120 | 0 |  |  |  |
| store_count | int | 4 | 0 |  |  |  |
| src_extrct_dt | datetime | 8 | 0 |  |  |  |
| upd_dt | datetime | 8 | 1 |  |  |  |
| etl_log_id | int | 4 | 0 |  |  |  |
| etl_evnt_id | int | 4 | 0 |  |  |  |
