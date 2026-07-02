# dbo.tmpPostWaveAllocationsAdjWM

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_no | varchar | 20 | 1 |  |  |  |
| distribution_line_no | varchar | 25 | 1 |  |  |  |
| upc_no | varchar | 14 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| allocated_units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputWMPostWaveAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingOutputWMPostWaveAllocAdj.md)
- [me_01: dbo.spMerchandisingSelectWMPostWaveAllocAdj](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWMPostWaveAllocAdj.md)
- [me_01: dbo.spMerchandisingSelectWMPostWaveAllocAdj_D365](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWMPostWaveAllocAdj_D365.md)

