# dbo.Labor_Job_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_key | int | 4 | 0 | YES |  | Surrogate Key |
| descr | varchar | 100 | 0 |  |  |  |
| abrv | varchar | 50 | 0 |  |  | Abbreviation |
| wb_cd | varchar | 50 | 0 |  |  | Workbrain Code |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPD_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
