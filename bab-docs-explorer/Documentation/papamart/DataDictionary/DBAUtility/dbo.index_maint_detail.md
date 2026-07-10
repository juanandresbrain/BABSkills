# dbo.index_maint_detail

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ObjectName | char | 255 | 1 |  |  |  |
| ObjectId | int | 4 | 1 |  |  |  |
| IndexName | char | 255 | 1 |  |  |  |
| IndexID | int | 4 | 1 |  |  |  |
| Lvl | int | 4 | 1 |  |  |  |
| CountPages | int | 4 | 1 |  |  |  |
| CountRows | int | 4 | 1 |  |  |  |
| MinRecSize | int | 4 | 1 |  |  |  |
| MaxRecSize | int | 4 | 1 |  |  |  |
| AvgRecSize | int | 4 | 1 |  |  |  |
| ForRecCount | int | 4 | 1 |  |  |  |
| Extents | int | 4 | 1 |  |  |  |
| ExtentSwitches | int | 4 | 1 |  |  |  |
| AvgFreeBytes | int | 4 | 1 |  |  |  |
| AvgPageDensity | int | 4 | 1 |  |  |  |
| SacDensity | decimal | 9 | 1 |  |  |  |
| BestCount | int | 4 | 1 |  |  |  |
| ActualCount | int | 4 | 1 |  |  |  |
| LogicalFrag | decimal | 9 | 1 |  |  |  |
| ExtentFrag | decimal | 9 | 1 |  |  |  |
| DBName | nvarchar | 256 | 1 |  |  |  |
