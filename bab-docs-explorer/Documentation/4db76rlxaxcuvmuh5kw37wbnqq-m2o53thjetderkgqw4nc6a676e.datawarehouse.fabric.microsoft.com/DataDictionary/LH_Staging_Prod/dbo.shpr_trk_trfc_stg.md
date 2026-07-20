# dbo.shpr_trk_trfc_stg

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SHPR_TRK_ORG_ID | decimal | 9 | 1 |  |  |  |
| SHPR_TRK_FL_LOG_ID | int | 4 | 1 |  |  |  |
| CUST_ID | int | 4 | 1 |  |  |  |
| DT | varchar | 8000 | 1 |  |  |  |
| TM | varchar | 8000 | 1 |  |  |  |
| ENTERS | int | 4 | 1 |  |  |  |
| EXITS | int | 4 | 1 |  |  |  |
| DATA_IND | varchar | 8000 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
