# BQ.BrickEngraving

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BQBrickID | int | 4 | 0 | YES |  |  |
| OrderNumber | varchar | 10 | 0 |  |  |  |
| sku | varchar | 50 | 0 |  |  |  |
| EngraveLine1 | varchar | 50 | 1 |  |  |  |
| EngraveLine2 | varchar | 50 | 1 |  |  |  |
| EngraveLine3 | varchar | 50 | 1 |  |  |  |
| EngraveName | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

