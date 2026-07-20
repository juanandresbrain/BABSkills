# dbo.emailrevenuedataroma

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendID | int | 4 | 1 |  |  |  |
| SendDate | datetime2 | 8 | 1 |  |  |  |
| Subject | varchar | 8000 | 1 |  |  |  |
| EmailName | varchar | 8000 | 1 |  |  |  |
| RetailRevenue1Summed | decimal | 17 | 1 |  |  |  |
| RetailRevenue2Summed | decimal | 17 | 1 |  |  |  |
| RetailRevenue3Summed | decimal | 17 | 1 |  |  |  |
| WebRevenue1Summed | decimal | 17 | 1 |  |  |  |
| WebRevenue2Summed | decimal | 17 | 1 |  |  |  |
| WebRevenue3Summed | decimal | 17 | 1 |  |  |  |
| RetailRevenueSummed | decimal | 17 | 1 |  |  |  |
| WebRevenueSummed | decimal | 17 | 1 |  |  |  |
| OmniRevenueSummed | decimal | 17 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
