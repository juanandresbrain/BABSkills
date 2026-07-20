# dbo.tmpazurepartitiongroups

**Database:** LH_Temp  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableName | varchar | 8000 | 1 |  |  |  |
| PartitionName | varchar | 8000 | 1 |  |  |  |
| PartitionRefreshedTime | varchar | 8000 | 1 |  |  |  |
| GroupNum | int | 4 | 1 |  |  |  |
| TableType | varchar | 8000 | 1 |  |  |  |
| PartitionedTable | int | 4 | 1 |  |  |  |
| PartitionState | bigint | 8 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| StopDate | date | 3 | 1 |  |  |  |
| CurrentPartition | int | 4 | 1 |  |  |  |
| LMPartition | int | 4 | 1 |  |  |  |
| LYPartition | int | 4 | 1 |  |  |  |
| LYLMPartition | int | 4 | 1 |  |  |  |
| TotalTableRowCount | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
