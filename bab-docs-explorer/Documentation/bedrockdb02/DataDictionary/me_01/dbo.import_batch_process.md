# dbo.import_batch_process

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_batch_process_id | decimal | 9 | 0 | YES |  |  |
| job_type | int | 4 | 0 |  |  |  |
| process_date | smalldatetime | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_asn_complete_$sp](../../StoredProcedures/me_01/dbo.import_asn_complete_$sp.md)
- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.import_pc_purge_$sp](../../StoredProcedures/me_01/dbo.import_pc_purge_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.purge_im_sale_$sp](../../StoredProcedures/me_01/dbo.purge_im_sale_$sp.md)
- [me_01: dbo.purge_imp_asn_$sp](../../StoredProcedures/me_01/dbo.purge_imp_asn_$sp.md)

