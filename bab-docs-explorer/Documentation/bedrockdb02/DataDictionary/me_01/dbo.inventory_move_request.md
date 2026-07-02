# dbo.inventory_move_request

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_move_request_id | decimal | 9 | 0 | YES |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| to_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| po_id | decimal | 9 | 1 |  |  |  |
| document_type | smallint | 2 | 0 |  |  |  |
| return_authorization_no | nvarchar | 40 | 1 |  |  |  |
| begin_send_date | smalldatetime | 4 | 1 |  |  |  |
| end_send_date | smalldatetime | 4 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| submit_date | smalldatetime | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)

