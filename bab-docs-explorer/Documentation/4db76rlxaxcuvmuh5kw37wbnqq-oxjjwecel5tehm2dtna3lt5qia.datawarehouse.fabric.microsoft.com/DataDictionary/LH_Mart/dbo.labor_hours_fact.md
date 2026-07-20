# dbo.labor_hours_fact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| emp_key | int | 4 | 1 |  |  |  |
| job_key | int | 4 | 1 |  |  |  |
| HOURTYPE_KEY | int | 4 | 1 |  |  |  |
| timecode_key | int | 4 | 1 |  |  |  |
| start_Time | datetime2 | 8 | 1 |  |  |  |
| end_Time | datetime2 | 8 | 1 |  |  |  |
| wrkd_minutes | int | 4 | 1 |  |  |  |
| source_system | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| ETL_LOG_ID | int | 4 | 1 |  |  |  |
| ETL_EVNT_ID | int | 4 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| wrkd_id | int | 4 | 1 |  |  |  |
