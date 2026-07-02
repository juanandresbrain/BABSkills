# dbo.ERP_DynamicsShipmentStage_UK

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipment | varchar | 52 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| ship_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 12 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| req_qty | int | 4 | 1 |  |  |  |
| sent_qty | int | 4 | 1 |  |  |  |
| variance_qty | int | 4 | 1 |  |  |  |
| carton_nbr | varchar | 20 | 1 |  |  |  |
| rec_type | varchar | 10 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |
| erd_date | varchar | 30 | 1 |  |  |  |
| insert_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)

