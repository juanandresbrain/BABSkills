# dbo.AzureTableMeta

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableName | nvarchar | 510 | 1 |  |  |  |
| TableModifiedTime | varchar | 100 | 1 |  |  |  |
| TableStructureModifiedTime | varchar | 100 | 1 |  |  |  |
| PartitionName | nvarchar | 510 | 1 |  |  |  |
| QueryDefinition | nvarchar | -1 | 1 |  |  |  |
| PartitionModifiedTime | varchar | 100 | 1 |  |  |  |
| PartitionRefreshedTime | varchar | 100 | 1 |  |  |  |
| State | bigint | 8 | 1 |  |  |  |
| Rows_Count | bigint | 8 | 1 |  |  |  |
