# dbo.backupmediafamily

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| media_set_id | int | 4 | 0 | YES | YES |  |
| family_sequence_number | tinyint | 1 | 0 | YES |  |  |
| media_family_id | uniqueidentifier | 16 | 1 |  |  |  |
| media_count | int | 4 | 1 |  |  |  |
| logical_device_name | nvarchar | 256 | 1 |  |  |  |
| physical_device_name | nvarchar | 520 | 1 |  |  |  |
| device_type | tinyint | 1 | 1 |  |  |  |
| physical_block_size | int | 4 | 1 |  |  |  |
| mirror | tinyint | 1 | 0 | YES |  |  |

