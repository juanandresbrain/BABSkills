# dbo.AvalaraExportControl

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FiscalYearPeriod | varchar | 60 | 1 |  |  |  |
| PeriodStartDate | varchar | 10 | 1 |  |  |  |
| PeriodEnddate | varchar | 10 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| USAFileNameOutput | varchar | 150 | 1 |  |  |  |
| CANFileNameOutput | varchar | 150 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
