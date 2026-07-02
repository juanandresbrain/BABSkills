# dbo.inpt_DBSchenkerScoutBookedPOLines

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 1 |  |  |  |
| po_shipment_line | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| qty | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingBulkInsertDBSchenkerASNFiles](../../StoredProcedures/me_01/dbo.spMerchandisingBulkInsertDBSchenkerASNFiles.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_2_BulkInsertASN](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_2_BulkInsertASN.md)

