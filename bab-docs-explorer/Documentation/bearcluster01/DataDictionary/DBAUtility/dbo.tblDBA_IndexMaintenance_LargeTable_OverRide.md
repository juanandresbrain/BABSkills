# dbo.tblDBA_IndexMaintenance_LargeTable_OverRide

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LargeTableID | int | 4 | 0 | YES |  |  |
| DatabaseName | varchar | 200 | 0 |  |  |  |
| SchemaName | varchar | 200 | 0 |  |  |  |
| TableName | varchar | 200 | 0 |  |  |  |
| DatabaseID | int | 4 | 0 |  |  |  |
| TableID | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spDBA_IndexOptimize_IntermediateNodes](../../StoredProcedures/DBAUtility/dbo.spDBA_IndexOptimize_IntermediateNodes.md)

