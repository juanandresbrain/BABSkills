# dbo.azure_traffic_fact

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| TrafficDate | date | 3 | 1 |  |  |  |
| TrafficHour | int | 4 | 1 |  |  |  |
| Traffic | bigint | 8 | 1 |  |  |  |
| HasDailyTraffic | int | 4 | 1 |  |  |  |
| TrafficDateTime | datetime2 | 8 | 1 |  |  |  |
