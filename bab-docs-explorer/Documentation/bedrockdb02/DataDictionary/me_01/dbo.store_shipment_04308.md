# dbo.store_shipment_04308

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_shipment_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| from_location_id | smallint | 2 | 0 |  |  |  |
| unit_weight_id | tinyint | 1 | 1 |  |  |  |
| document_no | varchar | 20 | 0 |  |  |  |
| document_status | smallint | 2 | 1 |  |  |  |
| state_no | int | 4 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 0 |  |  |  |
| receive_date | smalldatetime | 4 | 1 |  |  |  |
| performed_by | varchar | 60 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| external_system_name | varchar | 20 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| print_flag | bit | 1 | 0 |  |  |  |

