# dbo.Sv_Parameter

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 | YES |  |  |
| db_group_id | int | 4 | 0 | YES |  |  |
| app_id | int | 4 | 0 | YES |  |  |
| parameter_key | varchar | 30 | 0 | YES |  |  |
| parameter_value | varchar | 50 | 1 |  |  |  |
| label_1 | varchar | 60 | 1 |  |  |  |
| label_2 | varchar | 60 | 1 |  |  |  |
| description_1 | varchar | 255 | 1 |  |  |  |
| description_2 | varchar | 255 | 1 |  |  |  |
| max_value | varchar | 50 | 1 |  |  |  |
| min_value | varchar | 50 | 1 |  |  |  |
| default_value | varchar | 50 | 0 |  |  |  |
| data_type | varchar | 20 | 0 |  |  |  |
| parameter_modifiable | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CacheAllocate](../../StoredProcedures/fn_01/dbo.Sv_CacheAllocate.md)
- [smartlook_01: dbo.Sv_CacheAllocate](../../StoredProcedures/smartlook_01/dbo.Sv_CacheAllocate.md)

