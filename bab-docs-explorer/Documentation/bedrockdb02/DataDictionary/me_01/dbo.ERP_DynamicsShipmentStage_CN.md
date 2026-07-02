# dbo.ERP_DynamicsShipmentStage_CN

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fromLocation | varchar | 4 | 1 |  |  |  |
| document_no | varchar | 10 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| date_shipped | varchar | 10 | 1 |  |  |  |
| distribution_no | varchar | 12 | 1 |  |  |  |
| distribution_line | int | 4 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| ordered_qty | int | 4 | 1 |  |  |  |
| shipped_qty | int | 4 | 1 |  |  |  |
| variance_qty | int | 4 | 1 |  |  |  |
| carton_no | varchar | 20 | 1 |  |  |  |
| rec_type | int | 4 | 1 |  |  |  |
| external_system_name | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessCNShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessCNShipmentsAllocAdj.md)

