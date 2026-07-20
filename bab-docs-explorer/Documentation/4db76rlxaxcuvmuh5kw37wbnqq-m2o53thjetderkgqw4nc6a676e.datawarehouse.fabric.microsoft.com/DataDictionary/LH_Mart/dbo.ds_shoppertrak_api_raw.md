# dbo.ds_shoppertrak_api_raw

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| run_id | varchar | 8000 | 1 |  |  |  |
| ingest_ts | varchar | 8000 | 1 |  |  |  |
| start_date_yyyymmdd | varchar | 8000 | 1 |  |  |  |
| end_date_yyyymmdd | varchar | 8000 | 1 |  |  |  |
| group_by | varchar | 8000 | 1 |  |  |  |
| http_status | int | 4 | 1 |  |  |  |
| api_url | varchar | 8000 | 1 |  |  |  |
| api_params_json | varchar | 8000 | 1 |  |  |  |
| payload_xml | varchar | 8000 | 1 |  |  |  |
