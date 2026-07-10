# dbo.rtpWebOrderDataStage1

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreateDate | date | 3 | 1 |  |  |  |
| StatusDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 32 | 1 |  |  |  |
| ShipToState | nvarchar | 100 | 1 |  |  |  |
| ShipToCountry | nvarchar | 100 | 1 |  |  |  |
| TrackingNumber | varchar | 50 | 1 |  |  |  |
| Shipping | money | 8 | 1 |  |  |  |
| SiteCode | varchar | 10 | 1 |  |  |  |
