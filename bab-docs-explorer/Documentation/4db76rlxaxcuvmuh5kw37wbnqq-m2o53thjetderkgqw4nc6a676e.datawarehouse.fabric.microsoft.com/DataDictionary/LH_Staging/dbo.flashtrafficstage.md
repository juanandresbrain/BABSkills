# dbo.flashtrafficstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| storeID | int | 4 | 1 |  |  |  |
| exits | int | 4 | 1 |  |  |  |
| enters | int | 4 | 1 |  |  |  |
| startTime | varchar | 8000 | 1 |  |  |  |
| insert_datetime | datetime2 | 8 | 1 |  |  |  |
| HTTPString | varchar | 8000 | 1 |  |  |  |
