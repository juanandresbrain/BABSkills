# dbo.po_mass_mod_header

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mass_modification_id | decimal | 9 | 0 | YES |  |  |
| description | nvarchar | 120 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  | YES |  |
| order_date | datetime | 8 | 1 |  |  |  |
| system_cancel_date | datetime | 8 | 1 |  |  |  |
| from_delivery_date | datetime | 8 | 1 |  |  |  |
| to_delivery_date | datetime | 8 | 1 |  |  |  |
| reference_po_no | nvarchar | 40 | 1 |  |  |  |
| new_store_flag | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| expected_receipt_date | datetime | 8 | 1 |  |  |  |
| expected_receipt_date_days | smallint | 2 | 1 |  |  |  |

