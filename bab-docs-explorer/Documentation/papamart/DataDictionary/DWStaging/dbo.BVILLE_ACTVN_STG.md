# dbo.BVILLE_ACTVN_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BVILLE_ACTVN_STG_ID | int | 4 | 0 | YES |  |  |
| STR_NBR | int | 4 | 1 |  |  |  |
| TRN_NBR | int | 4 | 1 |  |  |  |
| TRN_START_DT | datetime | 8 | 1 |  |  |  |
| SRC_EXTRCT_DT | datetime | 8 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
