# dbo.temp_sales_markdown_audit

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| register | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_line | smallint | 2 | 1 |  |  |  |
| transaction_type | nvarchar | 40 | 1 |  |  |  |
| units_affected | int | 4 | 0 |  |  |  |
| sold_price_valuation | decimal | 9 | 0 |  |  |  |
| sold_price_selling | decimal | 9 | 0 |  |  |  |
| pos_md_variance_valuation | decimal | 9 | 0 |  |  |  |
| pos_md_variance_selling | decimal | 9 | 0 |  |  |  |
| pos_md_override_valuation | decimal | 9 | 0 |  |  |  |
| pos_md_override_selling | decimal | 9 | 0 |  |  |  |
| pos_discount_amount_valuation | decimal | 9 | 0 |  |  |  |
| pos_discount_amount_selling | decimal | 9 | 0 |  |  |  |
| promo_md_valuation | decimal | 9 | 0 |  |  |  |
| promo_md_selling | decimal | 9 | 0 |  |  |  |
| tax_amount_valuation | decimal | 9 | 1 |  |  |  |
| tax_amount_selling | decimal | 9 | 1 |  |  |  |
| exchange_rate_difference | decimal | 9 | 1 |  |  |  |
| price_override_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.populate_tmp_sale_md_audit_$sp](../../StoredProcedures/me_01/dbo.populate_tmp_sale_md_audit_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)

