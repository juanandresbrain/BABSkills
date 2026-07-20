# dbo.addr_stg

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ADDR_STG_ID | int | 4 | 1 |  |  |  |
| DTA_SET_CD | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| CLNSD_ADDR_ID | int | 4 | 1 |  |  |  |
| STG_DTA_SET_CD | varchar | 8000 | 1 |  |  |  |
| STG_ID | int | 4 | 1 |  |  |  |
