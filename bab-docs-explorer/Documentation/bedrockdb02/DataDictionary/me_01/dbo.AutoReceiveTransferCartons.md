# dbo.AutoReceiveTransferCartons

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| a | varchar | 2 | 0 |  |  |  |
| b | varchar | 1 | 0 |  |  |  |
| c | nvarchar | 40 | 1 |  |  |  |
| d | nvarchar | 40 | 0 |  |  |  |
| e | varchar | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers.md)
- [me_01: dbo.spMerchandisingSelectTransferCartons](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCartons.md)

