# dbo.tmpUKShipmentImport20131221Files

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipment | varchar | 52 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| ship_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 6 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| req_qty | int | 4 | 1 |  |  |  |
| sent_qty | int | 4 | 1 |  |  |  |
| variance_qty | int | 4 | 1 |  |  |  |
| carton_nbr | varchar | 25 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |
| erd_date | varchar | 30 | 1 |  |  |  |

