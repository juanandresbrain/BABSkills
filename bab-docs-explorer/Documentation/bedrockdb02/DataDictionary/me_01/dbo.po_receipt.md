# dbo.po_receipt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_receipt_id | decimal | 9 | 0 | YES |  |  |
| po_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| container_type_id | smallint | 2 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| advance_shipping_notice_id | decimal | 9 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| packing_list_no | nvarchar | 40 | 1 |  |  |  |
| packing_list_date | smalldatetime | 4 | 1 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| freight_amount | decimal | 9 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| payment_method | int | 4 | 1 |  |  |  |
| appointment_no | nvarchar | 12 | 1 |  |  |  |
| priority | nvarchar | 2 | 1 |  |  |  |
| bol_total_cartons | int | 4 | 1 |  |  |  |
| allocation_replaced_flag | bit | 1 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| match_status | smallint | 2 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| ticket_source | smallint | 2 | 0 |  |  |  |
| ticket_status | smallint | 2 | 0 |  |  |  |
| shipped_date | smalldatetime | 4 | 1 |  |  |  |
| track_in_transit_flag | bit | 1 | 0 |  |  |  |
| discrepancy_posted | smallint | 2 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.pom_check_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_check_released_units_$sp.md)
- [me_01: dbo.pom_retrieve_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_retrieve_released_units_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.spMerchandisingEmailPOReceiptMexico](../../StoredProcedures/me_01/dbo.spMerchandisingEmailPOReceiptMexico.md)
- [me_01: dbo.spMerchandisingPrintTransferCAPO](../../StoredProcedures/me_01/dbo.spMerchandisingPrintTransferCAPO.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)
- [me_01: dbo.spMerchandisingSelectTransferCAPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCAPO.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

