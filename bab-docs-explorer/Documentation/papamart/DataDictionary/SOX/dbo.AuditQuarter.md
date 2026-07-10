# dbo.AuditQuarter

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditQuarterKey | smallint | 2 | 0 | YES |  |  |
| AuditYear | smallint | 2 | 0 |  |  |  |
| AuditQuarter | tinyint | 1 | 0 |  |  |  |
| StartDateKey | smallint | 2 | 1 |  |  |  |
| EndDateKey | smallint | 2 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| EndDate | date | 3 | 1 |  |  |  |
