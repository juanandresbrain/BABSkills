# dbo.unsolicited_receipt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| unsolicited_receipt_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| container_type_id | smallint | 2 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| terms_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_no | nvarchar | 40 | 0 |  |  |  |
| document_description | nvarchar | 120 | 1 |  |  |  |
| document_status | smallint | 2 | 0 |  |  |  |
| grouping_label | nvarchar | 40 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | nvarchar | 120 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_doc_no | nvarchar | 40 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| match_status | smallint | 2 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| ticket_status | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)

