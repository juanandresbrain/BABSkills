# dbo.rptInventory

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationType | varchar | 10 | 1 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| style_desc | nvarchar | 240 | 1 |  |  |  |
| EOPOnHandUnitsTotalCurrent | int | 4 | 0 |  |  |  |
| EOPOnHandUnitsTotalLast1WeekLY | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.spMerchandisingTopStyleStage](../../StoredProcedures/ma_01/dbo.spMerchandisingTopStyleStage.md)

