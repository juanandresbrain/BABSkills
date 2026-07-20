# dbo.emailfact2017

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SubscriberKey | int | 4 | 1 |  |  |  |
| SendDate | datetime2 | 8 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| BounceDate | datetime2 | 8 | 1 |  |  |  |
| ClickDate | datetime2 | 8 | 1 |  |  |  |
| UnSubDate | datetime2 | 8 | 1 |  |  |  |
| OpenDate | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
