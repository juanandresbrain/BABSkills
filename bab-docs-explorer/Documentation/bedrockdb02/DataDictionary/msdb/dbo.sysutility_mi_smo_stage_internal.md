# dbo.sysutility_mi_smo_stage_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_type | int | 4 | 0 |  |  |  |
| urn | nvarchar | 8000 | 0 |  |  |  |
| property_name | nvarchar | 256 | 0 |  |  |  |
| property_value | sql_variant | 8016 | 1 |  |  |  |
| server_instance_name | sysname | 256 | 1 |  |  |  |
| physical_server_name | sysname | 256 | 1 |  |  |  |

