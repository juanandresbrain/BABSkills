# dbo.cn_qty_convert_1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| style | varchar | 6 | 1 |  |  |  |
| description | varchar | 52 | 1 |  |  |  |
| orig_qty | int | 4 | 1 |  |  |  |
| converted_qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingImportCNInvAdj](../../StoredProcedures/me_01/dbo.spMerchandisingImportCNInvAdj.md)
- [me_01: dbo.spMerchandisingImportCNInvAdj_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingImportCNInvAdj_Bak20210614.md)

