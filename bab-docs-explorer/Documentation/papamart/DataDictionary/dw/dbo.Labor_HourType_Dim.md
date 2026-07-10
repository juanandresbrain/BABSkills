# dbo.Labor_HourType_Dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| HourType_key | int | 4 | 0 | YES |  |  |
| descr | varchar | 100 | 0 |  |  |  |
| abrv | varchar | 50 | 0 |  |  |  |
| wb_cd | varchar | 50 | 0 |  |  |  |
| isPaid | bit | 1 | 0 |  |  |  |
| MULTPLIER | decimal | 5 | 0 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPD_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
