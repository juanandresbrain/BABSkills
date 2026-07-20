# dbo.rtpweborderdatastage1

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CreateDate | date | 3 | 1 |  |  |  |
| StatusDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| Shipping | decimal | 9 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
