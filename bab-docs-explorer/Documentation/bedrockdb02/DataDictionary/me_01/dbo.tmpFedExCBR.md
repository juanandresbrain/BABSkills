# dbo.tmpFedExCBR

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BC | varchar | 2 | 0 |  |  |  |
| A | varchar | 1 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| location | nvarchar | 40 | 0 |  |  |  |
| code | varchar | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputFedExReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts.md)
- [me_01: dbo.spMerchandisingOutputFedExReceipts_NEW20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts_NEW20230125.md)
- [me_01: dbo.spMerchandisingOutputFedExReceiptsBAK20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceiptsBAK20230125.md)

