# dbo.etl_prcs_cntrl_UseCase

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ETL_PRCS_ID | int | 4 | 0 |  |  |  |
| ETL_PRCS_NM | varchar | 50 | 1 |  |  |  |
| LAST_TS | datetime | 8 | 1 |  |  |  |
| LAST_ID | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
