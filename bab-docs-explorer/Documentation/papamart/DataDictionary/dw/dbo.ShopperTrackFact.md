# dbo.ShopperTrackFact

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShopperTrackFactKey | int | 4 | 0 | YES |  |  |
| ShopperTrakOrgId | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TimeKey | int | 4 | 1 |  |  |  |
| Enters | int | 4 | 1 |  |  |  |
| Exits | int | 4 | 1 |  |  |  |
| DataIndicatorName | varchar | 25 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
