# dbo.ib_intrastat

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_intrastat_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| cost | decimal | 9 | 0 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)

