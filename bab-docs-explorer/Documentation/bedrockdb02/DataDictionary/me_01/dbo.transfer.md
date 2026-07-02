# dbo.transfer

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transfer_id | decimal | 9 | 0 | YES |  |  |
| container_type_id | smallint | 2 | 1 |  |  |  |
| inventory_move_request_id | decimal | 9 | 1 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 0 |  |  |  |
| from_location_id | smallint | 2 | 0 |  |  |  |
| to_location_id | smallint | 2 | 0 |  |  |  |
| from_loc_address_type_id | smallint | 2 | 1 |  |  |  |
| to_loc_address_type_id | smallint | 2 | 1 |  |  |  |
| warehouse_id | smallint | 2 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| begin_send_date | smalldatetime | 4 | 1 |  |  |  |
| end_send_date | smalldatetime | 4 | 1 |  |  |  |
| manifest_no | nvarchar | 40 | 1 |  |  |  |
| receive_create_date | smalldatetime | 4 | 1 |  |  |  |
| packed_by | nvarchar | 120 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 1 |  |  |  |
| bill_of_lading | nvarchar | 40 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| cross_ref | nvarchar | 40 | 1 |  |  |  |
| routed_by_warehouse_flag | bit | 1 | 0 |  |  |  |
| received_by_warehouse_flag | bit | 1 | 0 |  |  |  |
| shipped_by_warehouse_flag | bit | 1 | 0 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dant_DamageTransfersWithoutCartonNumbers](../../StoredProcedures/me_01/dbo.dant_DamageTransfersWithoutCartonNumbers.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingProcessAutoReceiveInterCompanyTransfers.md)
- [me_01: dbo.spMerchandisingProcessWcStockAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWcStockAdj.md)
- [me_01: dbo.spMerchandisingSelectCAPOCBR](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCAPOCBR.md)
- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)
- [me_01: dbo.spMerchandisingSelectPoolPointTransferReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPoolPointTransferReceipts.md)
- [me_01: dbo.spMerchandisingSelectTransferCartons](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCartons.md)
- [me_01: dbo.spMerchandisingSelectUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKPOReceipts.md)
- [me_01: dbo.spMerchandisingSelectUnreceivedTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUnreceivedTransfers.md)
- [me_01: dbo.spMerchandisingTransferImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingTransferImportValidation.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

