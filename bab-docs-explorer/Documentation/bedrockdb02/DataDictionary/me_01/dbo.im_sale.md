# dbo.im_sale

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| im_sale_number | decimal | 13 | 0 |  |  |  |
| entry_no | decimal | 9 | 0 |  |  |  |
| transaction_line | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| register | smallint | 2 | 1 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
| aw_transaction_type | smallint | 2 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| price_override | bit | 1 | 1 |  |  |  |
| aw_reason_code | smallint | 2 | 1 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| sold_at_price | decimal | 9 | 0 |  |  |  |
| pos_discount_type_code | smallint | 2 | 1 |  |  |  |
| pos_discount_amount | decimal | 9 | 1 |  |  |  |
| tax_amount | decimal | 9 | 1 |  |  |  |
| originating_location_id | smallint | 2 | 1 |  |  |  |
| credit_originating_store | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.create_jobs_sales_posting_$sp](../../StoredProcedures/me_01/dbo.create_jobs_sales_posting_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.populate_temp_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.populate_temp_ib_inventory_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.populate_tmp_sale_md_audit_$sp](../../StoredProcedures/me_01/dbo.populate_tmp_sale_md_audit_$sp.md)
- [me_01: dbo.post_cust_order_return_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_return_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.prep_fixed_avg_cost_calculation_$sp](../../StoredProcedures/me_01/dbo.prep_fixed_avg_cost_calculation_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.purge_im_sale_$sp](../../StoredProcedures/me_01/dbo.purge_im_sale_$sp.md)

