# dbo.ta

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| StoreNumber | varchar | 10 | 1 |  |  |  |
| StoreLocator | varchar | 8000 | 1 |  |  |  |
| StoreMallWebsiteURL | varchar | 255 | 1 |  |  |  |
| SubChannel | nvarchar | 114 | 1 |  |  |  |
| Zone | varchar | 100 | 0 |  |  |  |
| PermCloseStatus | int | 4 | 0 |  |  |  |
| CalendarDate | date | 3 | 1 |  |  |  |
| CompDate | datetime | 8 | 1 |  |  |  |
| MallType | varchar | 255 | 1 |  |  |  |
| StoreType | varchar | 255 | 1 |  |  |  |
| StoreDesign | varchar | 255 | 1 |  |  |  |
| LocationType | varchar | 255 | 1 |  |  |  |
| PricingModel | varchar | 255 | 1 |  |  |  |
| Hispanic | varchar | 255 | 1 |  |  |  |
| OpenStatus | int | 4 | 1 |  |  |  |
| CompStatus | int | 4 | 1 |  |  |  |
| TrafficOpenStatus | int | 4 | 1 |  |  |  |
| TrafficCompStatus | int | 4 | 1 |  |  |  |
| ZoneDirector | varchar | 255 | 1 |  |  |  |
| DistrictManager | varchar | 255 | 1 |  |  |  |
| AreaManager | varchar | 255 | 1 |  |  |  |
