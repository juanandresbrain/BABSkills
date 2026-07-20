# dbo.canadalabordata

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
