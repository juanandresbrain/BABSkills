# dbo.tmpDetailCN

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 10 | 1 |  |  |  |
| distribution_no | varchar | 12 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| UPC_no | varchar | 42 | 1 |  |  |  |
| sent_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputCNshipments](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNshipments.md)

