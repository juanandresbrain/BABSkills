# dbo.CanadaLaborData

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LaborId | bigint | 8 | 0 | YES |  |  |
| StoreId | int | 4 | 0 |  |  |  |
| EmployeeId | int | 4 | 0 |  |  |  |
| ClockInDate | datetime | 8 | 0 |  |  |  |
| ClockOutDate | datetime | 8 | 0 |  |  |  |
| JobCode | varchar | 100 | 0 |  |  |  |
| Status | varchar | 100 | 0 |  |  |  |
| SourceFile | varchar | 255 | 0 |  |  |  |
| Processed | bit | 1 | 0 |  |  |  |
| ProcessLogId | int | 4 | 1 |  |  |  |
| RecordInsertedDateTime | datetime | 8 | 0 |  |  |  |
