# dbo.Sv_NextID

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_id | int | 4 | 0 | YES |  |  |
| table_name | varchar | 30 | 1 |  |  |  |
| next_id | int | 4 | 0 |  |  |  |
| max_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_GetNextID](../../StoredProcedures/fn_01/dbo.Sv_GetNextID.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_GetNextID](../../StoredProcedures/smartlook_01/dbo.Sv_GetNextID.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

