# dbo.imp_store_ship_rcpt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_store_ship_rcpt_id | decimal | 9 | 0 | YES |  |  |
| store_shipment_no | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| receive_by | nvarchar | 120 | 1 |  |  |  |
| receive_date | smalldatetime | 4 | 0 |  |  |  |

