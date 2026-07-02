# dbo.imp_store_shipment

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_store_shipment_id | decimal | 9 | 0 | YES |  |  |
| action | nvarchar | 2 | 0 |  |  |  |
| store_shipment_no | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| from_location_code | nvarchar | 40 | 0 |  |  |  |
| ship_date | smalldatetime | 4 | 0 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |

