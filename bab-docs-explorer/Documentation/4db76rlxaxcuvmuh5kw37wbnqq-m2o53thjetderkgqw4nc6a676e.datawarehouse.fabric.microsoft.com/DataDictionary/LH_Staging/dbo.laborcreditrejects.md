# dbo.laborcreditrejects

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DateSubmitted | varchar | 8000 | 1 |  |  |  |
| StoreNumber | varchar | 8000 | 1 |  |  |  |
| Month | varchar | 8000 | 1 |  |  |  |
| WeekNumber | varchar | 8000 | 1 |  |  |  |
| Credit | varchar | 8000 | 1 |  |  |  |
| Reason | varchar | 8000 | 1 |  |  |  |
| RequestedBy | varchar | 8000 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| RejectDate | datetime2 | 8 | 1 |  |  |  |
