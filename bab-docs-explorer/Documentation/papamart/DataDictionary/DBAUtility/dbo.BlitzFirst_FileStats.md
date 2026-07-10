# dbo.BlitzFirst_FileStats

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CheckDate | datetimeoffset | 10 | 1 |  |  |  |
| DatabaseID | int | 4 | 0 |  |  |  |
| FileID | int | 4 | 0 |  |  |  |
| DatabaseName | nvarchar | 512 | 1 |  |  |  |
| FileLogicalName | nvarchar | 512 | 1 |  |  |  |
| TypeDesc | nvarchar | 120 | 1 |  |  |  |
| SizeOnDiskMB | bigint | 8 | 1 |  |  |  |
| io_stall_read_ms | bigint | 8 | 1 |  |  |  |
| num_of_reads | bigint | 8 | 1 |  |  |  |
| bytes_read | bigint | 8 | 1 |  |  |  |
| io_stall_write_ms | bigint | 8 | 1 |  |  |  |
| num_of_writes | bigint | 8 | 1 |  |  |  |
| bytes_written | bigint | 8 | 1 |  |  |  |
| PhysicalName | nvarchar | 1040 | 1 |  |  |  |
