# dbo.shoppertrackfact

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShopperTrackFactKey | int | 4 | 1 |  |  |  |
| ShopperTrakOrgId | int | 4 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| DateKey | int | 4 | 1 |  |  |  |
| TimeKey | int | 4 | 1 |  |  |  |
| Enters | int | 4 | 1 |  |  |  |
| Exits | int | 4 | 1 |  |  |  |
| DataIndicatorName | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
