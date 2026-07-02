# dbo.po_sourcing_shipment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 | YES |  |  |
| po_sourcing_shipment_id | decimal | 9 | 0 |  |  |  |
| po_line_number | smallint | 2 | 0 | YES |  |  |
| po_line_number_shipment_number | int | 4 | 0 | YES |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| po_shipment_id  | smallint | 2 | 0 |  |  |  |

