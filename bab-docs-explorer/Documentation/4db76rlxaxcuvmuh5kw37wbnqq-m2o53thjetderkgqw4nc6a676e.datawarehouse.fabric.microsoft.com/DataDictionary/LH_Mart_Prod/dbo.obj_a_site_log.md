# dbo.obj_a_site_log

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| A_STLOG_N_ID | int | 4 | 1 |  |  |  |
| A_STLOG_N_LOGLEVEL | int | 4 | 1 |  |  |  |
| A_STLOG_D_LOGTIME | datetime2 | 8 | 1 |  |  |  |
| A_STLOG_C_LOGHOST | varchar | 8000 | 1 |  |  |  |
| A_STLOG_C_LOGMODUL | varchar | 8000 | 1 |  |  |  |
| A_STLOG_N_LOGPID | int | 4 | 1 |  |  |  |
| A_STLOG_C_LOGINFO | varchar | 8000 | 1 |  |  |  |
| A_STLOG_N_CLSTRID | int | 4 | 1 |  |  |  |
