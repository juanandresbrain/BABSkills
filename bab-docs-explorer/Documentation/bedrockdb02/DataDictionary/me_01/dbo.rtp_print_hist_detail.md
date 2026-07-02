# dbo.rtp_print_hist_detail

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
| last_printed_unit | decimal | 9 | 0 |  |  |  |
| unit_price | decimal | 9 | 0 |  |  |  |
| rtp_format_id | smallint | 2 | 0 |  |  |  |
| last_printed | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)

