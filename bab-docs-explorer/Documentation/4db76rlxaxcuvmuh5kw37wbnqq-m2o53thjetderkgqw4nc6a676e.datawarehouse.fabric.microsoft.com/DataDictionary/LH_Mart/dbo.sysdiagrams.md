# dbo.sysdiagrams

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | varchar | 8000 | 1 |  |  |  |
| principal_id | int | 4 | 1 |  |  |  |
| diagram_id | int | 4 | 1 |  |  |  |
| version | int | 4 | 1 |  |  |  |
| definition | varbinary | 8000 | 1 |  |  |  |
