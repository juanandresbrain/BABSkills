# dbo.CapacityPlanning

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CPID | int | 4 | 0 |  |  |  |
| ServerName | varchar | 15 | 0 |  |  |  |
| DatabaseName | varchar | 50 | 0 |  |  |  |
| ExecutionDateTime | datetime | 8 | 1 |  |  |  |
| NewDatabaseSize | decimal | 9 | 1 |  |  |  |
| OldDatabaseSize | decimal | 9 | 1 |  |  |  |
| NewCreationDate | datetime | 8 | 1 |  |  |  |
| OldCreationDate | datetime | 8 | 1 |  |  |  |
| VarDiff | decimal | 9 | 1 |  |  |  |
| PercentGrowth | decimal | 9 | 1 |  |  |  |
| AvgGrowth | decimal | 9 | 1 |  |  |  |
| DateDiff | decimal | 9 | 1 |  |  |  |
| Yr1DBProjections | decimal | 9 | 1 |  |  |  |
| Yr1LogProjections | decimal | 9 | 1 |  |  |  |
| Yr1DBProjections15Percent | decimal | 9 | 1 |  |  |  |
| Yr1LogProjections15Percent | decimal | 9 | 1 |  |  |  |
| Total1YrProj | decimal | 9 | 1 |  |  |  |
| Total1YrProj15Percent | decimal | 9 | 1 |  |  |  |
| Yr2DBProjections | decimal | 9 | 1 |  |  |  |
| Yr2LogProjections | decimal | 9 | 1 |  |  |  |
| Yr2DBProjections15Percent | decimal | 9 | 1 |  |  |  |
| Yr2LogProjections15Percent | decimal | 9 | 1 |  |  |  |
| Total2YrProj | decimal | 9 | 1 |  |  |  |
| Total2YrProj15Percent | decimal | 9 | 1 |  |  |  |
| Yr3DBProjections | decimal | 9 | 1 |  |  |  |
| Yr3LogProjections | decimal | 9 | 1 |  |  |  |
| Yr3DBProjections15Percent | decimal | 9 | 1 |  |  |  |
| Yr3LogProjections15Percent | decimal | 9 | 1 |  |  |  |
| Total3YrProj | decimal | 9 | 1 |  |  |  |
| Total3YrProj15Percent | decimal | 9 | 1 |  |  |  |
| TotalNumberofDatabases | int | 4 | 1 |  |  |  |

