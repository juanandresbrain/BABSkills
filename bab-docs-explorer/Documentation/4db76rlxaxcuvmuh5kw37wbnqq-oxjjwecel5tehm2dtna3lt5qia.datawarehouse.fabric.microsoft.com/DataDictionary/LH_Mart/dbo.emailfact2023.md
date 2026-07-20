# dbo.emailfact2023

**Database:** LH_Mart  
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
| retRev1 | decimal | 17 | 1 |  |  |  |
| webRev1 | decimal | 17 | 1 |  |  |  |
| retRev2 | decimal | 17 | 1 |  |  |  |
| webRev2 | decimal | 17 | 1 |  |  |  |
| retRev3 | decimal | 17 | 1 |  |  |  |
| webRev3 | decimal | 17 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| PromoCode | varchar | 8000 | 1 |  |  |  |
| ExprDate | datetime2 | 8 | 1 |  |  |  |
| Coupon | varchar | 8000 | 1 |  |  |  |
| StoreName | varchar | 8000 | 1 |  |  |  |
| LoyaltyMonth | int | 4 | 1 |  |  |  |
| DataSourceName | varchar | 8000 | 1 |  |  |  |
| FrequencyCount1m | int | 4 | 1 |  |  |  |
| FrequencyCount3m | int | 4 | 1 |  |  |  |
| FrequencyCount6m | int | 4 | 1 |  |  |  |
| FrequencyCount12m | int | 4 | 1 |  |  |  |
| FrequencyCount18m | int | 4 | 1 |  |  |  |
| FrequencyCount24m | int | 4 | 1 |  |  |  |
| FrequencyCountTtl | int | 4 | 1 |  |  |  |
| RecencyCount1m | int | 4 | 1 |  |  |  |
| RecencyCount3m | int | 4 | 1 |  |  |  |
| RecencyCount6m | int | 4 | 1 |  |  |  |
| RecencyCount12m | int | 4 | 1 |  |  |  |
| RecencyCount24m | int | 4 | 1 |  |  |  |
| RecencyCountTtl | int | 4 | 1 |  |  |  |
| MonetarySum1m | decimal | 17 | 1 |  |  |  |
| MonetarySum3m | decimal | 17 | 1 |  |  |  |
| MonetarySum6m | decimal | 17 | 1 |  |  |  |
| MonetarySum12m | decimal | 17 | 1 |  |  |  |
| MonetarySum18m | decimal | 17 | 1 |  |  |  |
| MonetarySum24m | decimal | 17 | 1 |  |  |  |
| MonetarySumTtl | decimal | 17 | 1 |  |  |  |
| AudienceSeg | varchar | 8000 | 1 |  |  |  |
| LastPurchaseDate | date | 3 | 1 |  |  |  |
| LastPurchaseChan | date | 3 | 1 |  |  |  |
| PreferredStory | varchar | 8000 | 1 |  |  |  |
| NewSubscriberKey | varchar | 8000 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
