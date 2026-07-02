# dbo.DBSchenkerScoutBookedPOLines

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 7 | 1 |  |  |  |
| po_shipment_line | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| qty | varchar | 20 | 1 |  |  |  |
| file_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingBulkInsertDBSchenkerASNFiles](../../StoredProcedures/me_01/dbo.spMerchandisingBulkInsertDBSchenkerASNFiles.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_2_BulkInsertASN](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_2_BulkInsertASN.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_4_PreviouslyCanceled](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_4_PreviouslyCanceled.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingSelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledPO.md)

