# dbo.import_startup_upc_error

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_startup_upc_id | decimal | 9 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| error_id | smallint | 2 | 0 |  |  |  |
| row_text | nvarchar | 1000 | 0 |  |  |  |
| classic_error | nvarchar | 1000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_import_upc_mod52_$sp](../../StoredProcedures/me_01/dbo.dl_import_upc_mod52_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.dl_vendor_upc_check_digit_calc_$sp](../../StoredProcedures/me_01/dbo.dl_vendor_upc_check_digit_calc_$sp.md)

