# dbo.CostcoFedExReceiptArchive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_nbr | varchar | 52 | 1 |  |  |  |
| tracking | varchar | 52 | 1 |  |  |  |
| carton_nbr | varchar | 52 | 1 |  |  |  |
| delivery_date | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailCostcoFedExReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingEmailCostcoFedExReceipts.md)

