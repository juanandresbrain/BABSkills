# dbo.tblDBA_SQLBlitzResults_old

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| InstanceName | varchar | 200 | 1 |  |  |  |
| CheckID | int | 4 | 1 |  |  |  |
| Priority | tinyint | 1 | 1 |  |  |  |
| FindingsGroup | varchar | 50 | 1 |  |  |  |
| Finding | varchar | 200 | 1 |  |  |  |
| Details | nvarchar | 8000 | 1 |  |  |  |
| RunDate | datetime | 8 | 1 |  |  |  |
| IsArchived | bit | 1 | 1 |  |  |  |
