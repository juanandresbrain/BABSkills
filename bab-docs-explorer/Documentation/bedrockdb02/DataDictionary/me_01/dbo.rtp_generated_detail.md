# dbo.rtp_generated_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_id | decimal | 9 | 0 | YES |  |  |
| document_type | tinyint | 1 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 | YES |  |  |
| style_color_id | decimal | 9 | 0 | YES |  |  |
| style_size_id | decimal | 9 | 0 | YES |  |  |
| tkt_unit | decimal | 9 | 0 |  |  |  |
| unit_price | decimal | 9 | 1 |  |  |  |
| rtp_format_id | smallint | 2 | 0 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |
| deleted_flag | bit | 1 | 0 |  |  |  |
| date_updated | smalldatetime | 4 | 0 |  |  |  |
| currency_symbol | nvarchar | 6 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.upd_pc_generate_tickets_$sp](../../StoredProcedures/me_01/dbo.upd_pc_generate_tickets_$sp.md)
- [me_01: dbo.validate_pc_generate_tickets_details_$sp](../../StoredProcedures/me_01/dbo.validate_pc_generate_tickets_details_$sp.md)

