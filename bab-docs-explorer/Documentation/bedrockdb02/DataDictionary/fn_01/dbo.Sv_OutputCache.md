# dbo.Sv_OutputCache

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cache_file_id | int | 4 | 0 |  |  |  |
| view_id | int | 4 | 0 |  |  |  |
| query_id | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| security_query_id | int | 4 | 0 |  |  |  |
| dynamic_query | varchar | 255 | 1 |  |  |  |
| qparameters_bag | varchar | 255 | 1 |  |  |  |
| created_datetime | datetime | 8 | 0 |  |  |  |
| valid_until | datetime | 8 | 0 |  |  |  |
| locked | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CacheAllocate](../../StoredProcedures/fn_01/dbo.Sv_CacheAllocate.md)
- [fn_01: dbo.Sv_CacheFindFileID](../../StoredProcedures/fn_01/dbo.Sv_CacheFindFileID.md)
- [smartlook_01: dbo.Sv_CacheAllocate](../../StoredProcedures/smartlook_01/dbo.Sv_CacheAllocate.md)
- [smartlook_01: dbo.Sv_CacheFindFileID](../../StoredProcedures/smartlook_01/dbo.Sv_CacheFindFileID.md)

