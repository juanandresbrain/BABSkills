# dbo.gl_account_segment_lookup

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| lookup_type | tinyint | 1 | 0 |  |  |  |
| lookup_from_value | int | 4 | 0 |  |  |  |
| lookup_to_value | int | 4 | 0 |  |  |  |
| gl_replacement_value | nvarchar | 40 | 0 |  |  |  |
