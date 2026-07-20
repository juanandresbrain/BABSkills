# dbo.babwmstr_time_zones_dim

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TM_ZN_ID | int | 4 | 1 |  |  |  |
| TM_ZN_CD | varchar | 8000 | 1 |  |  |  |
| DESCR | varchar | 8000 | 1 |  |  |  |
| OFFSET_TO_GMT | int | 4 | 1 |  |  |  |
| CRTED_BY | varchar | 8000 | 1 |  |  |  |
| CRTED_ON | datetime2 | 8 | 1 |  |  |  |
| UPDTD_BY | varchar | 8000 | 1 |  |  |  |
| UPDTD_ON | datetime2 | 8 | 1 |  |  |  |
