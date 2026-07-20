# dbo.tender_dim

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tender_key | int | 4 | 1 |  |  |  |
| tender_code | varchar | 8000 | 1 |  |  |  |
| tender_desc | varchar | 8000 | 1 |  |  |  |
| process_name | varchar | 8000 | 1 |  |  |  |
| process_date | datetime2 | 8 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
