# dbo.Sv_OutputNote

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 |  |  |  |
| page_number | int | 4 | 0 |  |  |  |
| note_text | varchar | 255 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| created_date | smalldatetime | 4 | 0 |  |  |  |
| positionX | float | 8 | 0 |  |  |  |
| positionY | float | 8 | 0 |  |  |  |
| note_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

