# dbo.tmpUDAerror

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| submit_date | smalldatetime | 4 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| transaction_reason_code | nvarchar | 10 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| units_to_adjust | int | 4 | 1 |  |  |  |
| error_msg | nvarchar | 250 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailImportUDAerrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailImportUDAerrors.md)

