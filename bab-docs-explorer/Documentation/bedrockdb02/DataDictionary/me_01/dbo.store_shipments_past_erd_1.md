# dbo.store_shipments_past_erd_1

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 20 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| warehouse | varchar | 20 | 0 |  |  |  |
| total_cartons | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning.md)
- [me_01: dbo.spMerchandisingEmail1DaysPastERDWarning_BAK](../../StoredProcedures/me_01/dbo.spMerchandisingEmail1DaysPastERDWarning_BAK.md)

