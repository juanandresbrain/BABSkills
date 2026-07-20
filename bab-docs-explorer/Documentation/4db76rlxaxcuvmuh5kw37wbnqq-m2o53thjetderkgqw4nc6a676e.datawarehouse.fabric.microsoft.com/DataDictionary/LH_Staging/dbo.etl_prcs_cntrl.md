# dbo.etl_prcs_cntrl

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
| STAT_CD | varchar | 8000 | 1 |  |  |  |
