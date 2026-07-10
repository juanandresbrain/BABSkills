# Azure.PCHealthChecks

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Hostname | nvarchar | 100 | 1 |  |  |  |
| Store | nvarchar | 8 | 1 |  |  |  |
| Role | nvarchar | 40 | 1 |  |  |  |
| Model | nvarchar | 100 | 1 |  |  |  |
| GoPostReportErrors | int | 4 | 1 |  |  |  |
| GoPostReportWarnings | int | 4 | 1 |  |  |  |
| Description | nvarchar | 200 | 1 |  |  |  |
| Status | nvarchar | 100 | 1 |  |  |  |
| DateTime | datetime | 8 | 1 |  |  |  |
| Date | date | 3 | 1 |  |  |  |
