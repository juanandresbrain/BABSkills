# dbo.rtv

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rtv_id | decimal | 9 | 0 | YES |  |  |
| container_type_id | smallint | 2 | 1 |  |  |  |
| inventory_move_request_id | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| terms_id | smallint | 2 | 0 |  |  |  |
| vendor_address_type_id | smallint | 2 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| returned_date | smalldatetime | 4 | 1 |  |  |  |
| request_date | smalldatetime | 4 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| insurance_amount_1 | decimal | 9 | 1 |  |  |  |
| freight_amount_1 | decimal | 9 | 1 |  |  |  |
| misc_amount_1 | decimal | 9 | 1 |  |  |  |
| insurance_amount_2 | decimal | 9 | 1 |  |  |  |
| freight_amount_2 | decimal | 9 | 1 |  |  |  |
| misc_amount_2 | decimal | 9 | 1 |  |  |  |
| return_authorization_no | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 1 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |
| match_status | smallint | 2 | 0 |  |  |  |
| credit_note_number | nvarchar | 40 | 1 |  |  |  |
| packed_by | nvarchar | 120 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)

