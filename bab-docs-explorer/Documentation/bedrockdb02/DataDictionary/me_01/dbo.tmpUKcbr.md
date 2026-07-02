# dbo.tmpUKcbr

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | nvarchar | 40 | 1 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectUKCBR](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKCBR.md)
- [me_01: dbo.spMerchandisingSelectUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKPOReceipts.md)

