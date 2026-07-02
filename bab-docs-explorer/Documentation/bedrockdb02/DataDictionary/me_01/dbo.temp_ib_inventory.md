# dbo.temp_ib_inventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| transaction_line | smallint | 2 | 1 |  |  |  |
| sale_md_audit_flag | bit | 1 | 0 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| credit_originating_store | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.populate_temp_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.populate_temp_ib_inventory_$sp.md)
- [me_01: dbo.populate_tmp_sale_md_audit_$sp](../../StoredProcedures/me_01/dbo.populate_tmp_sale_md_audit_$sp.md)
- [me_01: dbo.post_cust_order_return_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_return_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)

