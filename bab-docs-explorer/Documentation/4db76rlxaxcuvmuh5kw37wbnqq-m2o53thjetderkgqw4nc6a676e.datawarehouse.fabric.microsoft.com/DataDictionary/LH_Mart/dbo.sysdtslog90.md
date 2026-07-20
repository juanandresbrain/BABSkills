# dbo.sysdtslog90

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 1 |  |  |  |
| event | varchar | 8000 | 1 |  |  |  |
| computer | varchar | 8000 | 1 |  |  |  |
| operator | varchar | 8000 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| sourceid | varchar | 8000 | 1 |  |  |  |
| executionid | varchar | 8000 | 1 |  |  |  |
| starttime | datetime2 | 8 | 1 |  |  |  |
| endtime | datetime2 | 8 | 1 |  |  |  |
| datacode | int | 4 | 1 |  |  |  |
| databytes | varbinary | 8000 | 1 |  |  |  |
| message | varchar | 8000 | 1 |  |  |  |
