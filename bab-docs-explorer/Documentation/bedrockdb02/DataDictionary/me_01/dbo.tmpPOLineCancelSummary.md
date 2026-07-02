# dbo.tmpPOLineCancelSummary

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 0 |  |  |  |
| canceled_line | int | 4 | 0 |  |  |  |
| booked | varchar | 3 | 0 |  |  |  |
| new_line | int | 4 | 0 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_8_EmailSummaryAndException](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_8_EmailSummaryAndException.md)
- [me_01: dbo.spMerchandisingSelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledPO.md)

