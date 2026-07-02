# dbo.imp_user_def_adj

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_user_def_adj_id | decimal | 9 | 0 | YES |  |  |
| action | nchar | 2 | 0 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_reason_code | nvarchar | 10 | 0 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| two_sided_pseudo_style_adjust | nchar | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingEmailImportUDAerrors](../../StoredProcedures/me_01/dbo.spMerchandisingEmailImportUDAerrors.md)

