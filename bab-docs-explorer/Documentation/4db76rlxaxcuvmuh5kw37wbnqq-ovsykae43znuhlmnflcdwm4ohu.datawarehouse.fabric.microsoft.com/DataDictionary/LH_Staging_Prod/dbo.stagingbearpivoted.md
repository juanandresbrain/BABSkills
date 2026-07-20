# dbo.stagingbearpivoted

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StagingBearPivotedId | int | 4 | 1 |  |  |  |
| BearId | varchar | 8000 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| AttributeType | varchar | 8000 | 1 |  |  |  |
| AttributeValues | varchar | 8000 | 1 |  |  |  |
| Items | varchar | 8000 | 1 |  |  |  |
