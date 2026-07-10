# dbo.tblDBA_DatabaseIntegrityRepository

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrityHistoryID | int | 4 | 0 | YES |  |  |
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| ErrorNumber | int | 4 | 1 |  |  |  |
| ErrorLevel | int | 4 | 1 |  |  |  |
| DBState | int | 4 | 1 |  |  |  |
| Message_Text | nvarchar | 2048 | 1 |  |  |  |
| RepairLevel | int | 4 | 1 |  |  |  |
| DBStatus | int | 4 | 1 |  |  |  |
| ServerDBID | int | 4 | 1 |  |  |  |
| DBObjectID | int | 4 | 1 |  |  |  |
| IndexID | int | 4 | 1 |  |  |  |
| PartitionID | bigint | 8 | 1 |  |  |  |
| AllocationUnitID | bigint | 8 | 1 |  |  |  |
| DBFile | int | 4 | 1 |  |  |  |
| Page | int | 4 | 1 |  |  |  |
| Slot | int | 4 | 1 |  |  |  |
| RefFile | int | 4 | 1 |  |  |  |
| RefPage | int | 4 | 1 |  |  |  |
| RefSlot | int | 4 | 1 |  |  |  |
| Allocation | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
