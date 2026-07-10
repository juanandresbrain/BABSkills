# dbo.SHPR_TRK_TRFC_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SHPR_TRK_ORG_ID | numeric | 9 | 1 |  |  |  |
| SHPR_TRK_FL_LOG_ID | int | 4 | 1 |  |  |  |
| CUST_ID | int | 4 | 1 |  |  |  |
| DT | varchar | 8 | 1 |  |  |  |
| TM | varchar | 6 | 1 |  |  |  |
| ENTERS | int | 4 | 1 |  |  |  |
| EXITS | int | 4 | 1 |  |  |  |
| DATA_IND | char | 1 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
