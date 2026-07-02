# dbo.tblHearMeSalesConversionArchive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_inventory_id | decimal | 9 | 0 |  |  |  |
| proc_date | datetime | 8 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_number | varchar | 20 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |
| updated_flag | bit | 1 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_03082016](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_03082016.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.spHearMeSalesConversionBACKUP20150818](../../StoredProcedures/me_01/dbo.spHearMeSalesConversionBACKUP20150818.md)
- [me_01: dbo.spHearMeSalesConversionBACKUP20150818_TC_TEST](../../StoredProcedures/me_01/dbo.spHearMeSalesConversionBACKUP20150818_TC_TEST.md)

