# dbo.BlitzFirst_PerfmonStats

**Database:** DBAUtility  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CheckDate | datetimeoffset | 10 | 1 |  |  |  |
| object_name | nvarchar | 256 | 0 |  |  |  |
| counter_name | nvarchar | 256 | 0 |  |  |  |
| instance_name | nvarchar | 256 | 1 |  |  |  |
| cntr_value | bigint | 8 | 1 |  |  |  |
| cntr_type | int | 4 | 0 |  |  |  |
| value_delta | bigint | 8 | 1 |  |  |  |
| value_per_second | decimal | 9 | 1 |  |  |  |

