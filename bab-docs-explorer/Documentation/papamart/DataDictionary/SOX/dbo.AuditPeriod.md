# dbo.AuditPeriod

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditPeriodKey | smallint | 2 | 0 | YES |  |  |
| AuditYear | smallint | 2 | 0 |  |  |  |
| AuditPeriod | tinyint | 1 | 0 |  |  |  |
| StartDateKey | smallint | 2 | 1 |  |  |  |
| EndDateKey | smallint | 2 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| EndDate | date | 3 | 1 |  |  |  |
