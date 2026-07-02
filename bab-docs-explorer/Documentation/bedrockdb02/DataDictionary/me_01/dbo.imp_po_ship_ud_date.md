# dbo.imp_po_ship_ud_date

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_po_ship_ud_date_id | decimal | 9 | 0 |  |  |  |
| imp_po_id | decimal | 9 | 0 |  |  |  |
| action_type | nchar | 2 | 1 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| user_defined_date | smalldatetime | 4 | 0 |  |  |  |
| date_type_code | nvarchar | 6 | 0 |  |  |  |
| shipment_number | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| po_line_number | smallint | 2 | 1 |  |  |  |
| po_line_number_shipment_number | int | 4 | 0 |  |  |  |

