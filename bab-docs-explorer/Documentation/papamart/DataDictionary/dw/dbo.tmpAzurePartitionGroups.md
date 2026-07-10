# dbo.tmpAzurePartitionGroups

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableName | nvarchar | 510 | 1 |  |  |  |
| PartitionName | nvarchar | 510 | 1 |  |  |  |
| PartitionRefreshedTime | datetime | 8 | 1 |  |  |  |
| GroupNum | bigint | 8 | 1 |  |  |  |
| TableType | varchar | 11 | 0 |  |  |  |
| PartitionedTable | int | 4 | 0 |  |  |  |
| PartitionState | bigint | 8 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| StopDate | date | 3 | 1 |  |  |  |
| CurrentPartition | int | 4 | 0 |  |  |  |
| LMPartition | int | 4 | 0 |  |  |  |
| LYPartition | int | 4 | 0 |  |  |  |
| LYLMPartition | int | 4 | 0 |  |  |  |
| TotalTableRowCount | bigint | 8 | 1 |  |  |  |
