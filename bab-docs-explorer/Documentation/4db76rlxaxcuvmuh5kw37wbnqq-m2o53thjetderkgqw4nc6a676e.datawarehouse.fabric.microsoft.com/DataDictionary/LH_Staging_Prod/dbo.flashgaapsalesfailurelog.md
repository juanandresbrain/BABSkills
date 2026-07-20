# dbo.flashgaapsalesfailurelog

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreID | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| StoreIP | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| FailureReason | varchar | 8000 | 1 |  |  |  |
