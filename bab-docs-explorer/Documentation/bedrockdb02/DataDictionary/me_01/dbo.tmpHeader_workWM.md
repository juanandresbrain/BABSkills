# dbo.tmpHeader_workWM

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | varchar | 50 | 1 |  |  |  |
| date_shipped | varchar | 30 | 1 |  |  |  |
| day_shipped | int | 4 | 1 |  |  |  |
| transit_days | int | 4 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| external_system_name | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj.md)
- [me_01: dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingProcessWMShipmentsAllocAdj_D365.md)

