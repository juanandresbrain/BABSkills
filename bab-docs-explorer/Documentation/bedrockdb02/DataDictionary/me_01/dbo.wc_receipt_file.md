# dbo.wc_receipt_file

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| receipt_date | varchar | 8 | 1 |  |  |  |
| po_nbr | varchar | 52 | 1 |  |  |  |
| ref_nbr | varchar | 10 | 1 |  |  |  |
| style | varchar | 6 | 1 |  |  |  |
| qty_received | int | 4 | 1 |  |  |  |
| qty_damaged | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_Report_wcReceipts](../../StoredProcedures/me_01/dbo.spMerchandising_Report_wcReceipts.md)
- [me_01: dbo.spMerchandising_Select_wcPOreceipts](../../StoredProcedures/me_01/dbo.spMerchandising_Select_wcPOreceipts.md)
- [me_01: dbo.spMerchandising_Select_wcShipmentReceipts](../../StoredProcedures/me_01/dbo.spMerchandising_Select_wcShipmentReceipts.md)

