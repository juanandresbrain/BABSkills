# dbo.DTA_reports_indexcolumn

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IndexID | int | 4 | 0 |  | YES |  |
| ColumnID | int | 4 | 0 |  |  |  |
| ColumnOrder | int | 4 | 1 |  |  |  |
| PartitionColumnOrder | int | 4 | 0 |  |  |  |
| IsKeyColumn | bit | 1 | 0 |  |  |  |
| IsDescendingColumn | bit | 1 | 0 |  |  |  |

