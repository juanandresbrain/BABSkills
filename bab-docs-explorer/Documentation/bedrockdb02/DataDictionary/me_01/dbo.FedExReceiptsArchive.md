# dbo.FedExReceiptsArchive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tracking | varchar | 50 | 1 |  |  |  |
| carton_no | varchar | 50 | 1 |  |  |  |
| location | varchar | 50 | 1 |  |  |  |
| delivery_date | varchar | 50 | 1 |  |  |  |
| delivery_time | varchar | 50 | 1 |  |  |  |
| signature | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailCostcoFedExReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingEmailCostcoFedExReceipts.md)
- [me_01: dbo.spMerchandisingOutputFedExReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts.md)
- [me_01: dbo.spMerchandisingOutputFedExReceipts_NEW20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceipts_NEW20230125.md)
- [me_01: dbo.spMerchandisingOutputFedExReceiptsBAK20230125](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFedExReceiptsBAK20230125.md)

