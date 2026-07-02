# dbo.view2

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 |  |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |
| line_no | decimal | 9 | 1 |  |  |  |
| po_line_shipment_id | int | 4 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |

