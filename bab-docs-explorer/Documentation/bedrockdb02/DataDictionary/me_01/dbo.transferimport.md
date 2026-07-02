# dbo.transferimport

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_time | datetime | 8 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| from_location | varchar | 4 | 1 |  |  |  |
| to_location | varchar | 4 | 1 |  |  |  |
| date_shipped | varchar | 12 | 1 |  |  |  |
| reason_code | varchar | 5 | 1 |  |  |  |
| grouping_label | varchar | 20 | 1 |  |  |  |
| upc | varchar | 12 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| importfile | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputCNTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNTransfers.md)
- [me_01: dbo.spMerchandisingSelectCondosBalesDistrosAndTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCondosBalesDistrosAndTransfers.md)
- [me_01: dbo.spMerchandisingSelectPoolPointTransfer](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPoolPointTransfer.md)
- [me_01: dbo.spMerchandisingTransferImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingTransferImportValidation.md)

