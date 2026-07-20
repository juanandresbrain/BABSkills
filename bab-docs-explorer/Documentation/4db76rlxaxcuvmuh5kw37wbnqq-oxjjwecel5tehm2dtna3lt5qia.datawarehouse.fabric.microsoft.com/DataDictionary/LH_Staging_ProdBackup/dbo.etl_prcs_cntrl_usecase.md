# dbo.etl_prcs_cntrl_usecase

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETL_PRCS_ID | int | 4 | 1 |  |  |  |
| ETL_PRCS_NM | varchar | 8000 | 1 |  |  |  |
| LAST_TS | datetime2 | 8 | 1 |  |  |  |
| LAST_ID | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
