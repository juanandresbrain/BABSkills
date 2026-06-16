# dbo.tmpResults

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNum | varchar | 8000 | 1 |  |  |  |
| LicensePlate | varchar | 8000 | 1 |  |  |  |
| ItemNum | varchar | 8000 | 1 |  |  |  |
| ProductName | varchar | 8000 | 1 |  |  |  |
| ShipFrom | varchar | 8000 | 1 |  |  |  |
| ShipTo | varchar | 8000 | 1 |  |  |  |
| ProductHierarchy | varchar | 8000 | 0 |  |  |  |
| ShipDate | datetime2 | 8 | 1 |  |  |  |
| ItemQty | numeric | 9 | 1 |  |  |  |
| CartonQty | int | 4 | 1 |  |  |  |
| isMiscCarton | int | 4 | 0 |  |  |  |
| MiscCartonDetails | varchar | 8000 | 1 |  |  |  |

