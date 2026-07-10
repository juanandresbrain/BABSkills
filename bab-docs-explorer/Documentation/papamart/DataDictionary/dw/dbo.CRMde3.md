# dbo.CRMde3

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customerNumber | varchar | 20 | 1 |  |  |  |
| transactionID | int | 4 | 1 |  |  |  |
| purchaseDate | datetime | 8 | 1 |  |  |  |
| purchaseChannel | nvarchar | 40 | 1 |  |  |  |
| purchaseStoreNumber | nvarchar | 20 | 1 |  |  |  |
| purchaseRevenue | numeric | 17 | 1 |  |  |  |
| purchaseUnitCount | int | 4 | 1 |  |  |  |
| stuffed | int | 4 | 1 |  |  |  |
| unstuffed | int | 4 | 1 |  |  |  |
| licensedORNot | int | 4 | 1 |  |  |  |
| consumerGroup | varchar | 20 | 1 |  |  |  |
| keyStory | nvarchar | 60 | 1 |  |  |  |
| department | varchar | 20 | 1 |  |  |  |
| Country | varchar | 50 | 1 |  |  |  |
| sku | varchar | 20 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| recID | int | 4 | 0 | YES |  |  |
| Emailable | int | 4 | 1 |  |  |  |
