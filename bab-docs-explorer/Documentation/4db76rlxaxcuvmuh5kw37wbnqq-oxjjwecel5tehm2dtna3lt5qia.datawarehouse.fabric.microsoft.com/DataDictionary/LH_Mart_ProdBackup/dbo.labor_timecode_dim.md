# dbo.labor_timecode_dim

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| timeCode_key | int | 4 | 1 |  |  |  |
| descr | varchar | 8000 | 1 |  |  |  |
| abrv | varchar | 8000 | 1 |  |  |  |
| wb_cd | varchar | 8000 | 1 |  |  |  |
| isWork | bit | 1 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPD_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
