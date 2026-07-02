# dbo.im_4wall_po_receipt_xref

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_receipt_id | decimal | 9 | 0 | YES |  |  |
| cartons_received | int | 4 | 0 |  |  |  |
| units_expected | int | 4 | 0 |  |  |  |
| units_received | int | 4 | 0 |  |  |  |
| merchandise_status_code | nvarchar | 2 | 1 |  |  |  |
| date_posted | smalldatetime | 4 | 1 |  |  |  |

