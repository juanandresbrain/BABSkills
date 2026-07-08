# dbo.tblDBA_IndexMaintenance_LargeTable_Repository

**Database:** DBAUtility  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LargeTableID | int | 4 | 0 | YES |  |  |
| DatabaseName | varchar | 200 | 0 |  |  |  |
| SchemaName | varchar | 200 | 0 |  |  |  |
| TableName | varchar | 200 | 0 |  |  |  |
| IndexName | varchar | 200 | 0 |  |  |  |
| DatabaseID | int | 4 | 0 |  |  |  |
| TableID | int | 4 | 0 |  |  |  |
| IndexID | int | 4 | 0 |  |  |  |
| LastCheckDate | datetime | 8 | 0 |  |  |  |
| avg_fragmentation_in_percent | float | 8 | 0 |  |  |  |
| TimeSpent | varchar | 10 | 0 |  |  |  |
