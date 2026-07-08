# dbo.partition_merge

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| partition_function_name | nvarchar | 256 | 0 |  |  |  |
| partition_no | smallint | 2 | 0 |  |  |  |
| min_tran_date | smalldatetime | 4 | 0 |  |  |  |
| trans_qty | int | 4 | 1 |  |  |  |
