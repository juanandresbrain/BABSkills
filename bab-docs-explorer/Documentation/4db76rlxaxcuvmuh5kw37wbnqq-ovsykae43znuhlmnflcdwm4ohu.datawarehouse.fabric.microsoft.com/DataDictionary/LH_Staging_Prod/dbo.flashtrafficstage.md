# dbo.flashtrafficstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| storeID | int | 4 | 1 |  |  |  |
| exits | int | 4 | 1 |  |  |  |
| enters | int | 4 | 1 |  |  |  |
| startTime | varchar | 8000 | 1 |  |  |  |
| insert_datetime | datetime2 | 8 | 1 |  |  |  |
| HTTPString | varchar | 8000 | 1 |  |  |  |
