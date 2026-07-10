# dbo.tblDBA_SQLBlitzResults

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CheckDate | datetime | 8 | 1 |  |  |  |
| BlitzVersion | int | 4 | 1 |  |  |  |
| Priority | tinyint | 1 | 1 |  |  |  |
| FindingsGroup | varchar | 50 | 1 |  |  |  |
| Finding | varchar | 200 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| URL | varchar | 200 | 1 |  |  |  |
| Details | nvarchar | 8000 | 1 |  |  |  |
| QueryPlan | nvarchar | -1 | 1 |  |  |  |
| QueryPlanFiltered | nvarchar | -1 | 1 |  |  |  |
| CheckID | int | 4 | 1 |  |  |  |
