# dbo.metadata_refresh_log

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| refresh_id | varchar | 8000 | 1 |  |  |  |
| refresh_date | date | 3 | 1 |  |  |  |
| logged_date_time | datetime2 | 8 | 1 |  |  |  |
| is_successful | bit | 1 | 1 |  |  |  |
