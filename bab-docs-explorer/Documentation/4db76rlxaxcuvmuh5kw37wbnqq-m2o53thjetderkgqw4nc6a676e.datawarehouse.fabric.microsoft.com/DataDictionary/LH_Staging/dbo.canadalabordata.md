# dbo.canadalabordata

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LaborId | bigint | 8 | 1 |  |  |  |
| StoreId | int | 4 | 1 |  |  |  |
| EmployeeId | int | 4 | 1 |  |  |  |
| ClockInDate | datetime2 | 8 | 1 |  |  |  |
| ClockOutDate | datetime2 | 8 | 1 |  |  |  |
| JobCode | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| SourceFile | varchar | 8000 | 1 |  |  |  |
| Processed | bit | 1 | 1 |  |  |  |
| ProcessLogId | int | 4 | 1 |  |  |  |
| RecordInsertedDateTime | datetime2 | 8 | 1 |  |  |  |
