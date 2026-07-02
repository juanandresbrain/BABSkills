# dbo.configurations_snapshot

**Database:** master  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| configuration_id | int | 4 | 1 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| value | sql_variant | 8016 | 1 |  |  |  |
| minimum | sql_variant | 8016 | 1 |  |  |  |
| maximum | sql_variant | 8016 | 1 |  |  |  |
| value_in_use | sql_variant | 8016 | 1 |  |  |  |

