# dbo.user_partition

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| partition_scheme | nvarchar | 60 | 0 |  |  |  |
| min_value | nvarchar | 20 | 0 |  |  |  |
| max_value | nvarchar | 40 | 0 |  |  |  |
| last_used_filegroup | nvarchar | 60 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.add_partitions_$sp](../../StoredProcedures/ma_01/dbo.add_partitions_$sp.md)
- [ma_01: dbo.create_initial_history_partitions_$sp](../../StoredProcedures/ma_01/dbo.create_initial_history_partitions_$sp.md)

