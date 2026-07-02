# dbo.erd_matrix

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | nvarchar | 510 | 1 |  |  |  |
| rec_type | int | 4 | 1 |  |  |  |
| days | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectUKStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_Backup_06132017.md)
- [me_01: dbo.spMerchandisingSelectUKStoreShipments_BAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKStoreShipments_BAK20220731.md)

