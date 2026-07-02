# dbo.Sv_OutputIndexLabel

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| output_id | int | 4 | 0 |  |  |  |
| index_field_id | int | 4 | 0 |  |  |  |
| label | varchar | 60 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_OutputIndexLabel_Add](../../StoredProcedures/fn_01/dbo.Sv_OutputIndexLabel_Add.md)
- [smartlook_01: dbo.Sv_OutputIndexLabel_Add](../../StoredProcedures/smartlook_01/dbo.Sv_OutputIndexLabel_Add.md)

