# dbo.EmailFactStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SendDate | datetime | 8 | 1 |  |  |  |
| SubscriberKey | varchar | 200 | 1 |  |  |  |
| EmailAddress | varchar | 200 | 1 |  |  |  |
| BounceDate | datetime | 8 | 1 |  |  |  |
| ClickDate | datetime | 8 | 1 |  |  |  |
| UnSubDate | datetime | 8 | 1 |  |  |  |
| OpenDate | datetime | 8 | 1 |  |  |  |
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
| MonetarySum1m | numeric | 17 | 1 |  |  |  |
| MonetarySum3m | numeric | 17 | 1 |  |  |  |
| MonetarySum6m | numeric | 17 | 1 |  |  |  |
| MonetarySum12m | numeric | 17 | 1 |  |  |  |
| MonetarySum18m | numeric | 17 | 1 |  |  |  |
| MonetarySum24m | numeric | 17 | 1 |  |  |  |
| MonetarySumTtl | numeric | 17 | 1 |  |  |  |
| AudienceSeg | varchar | 100 | 1 |  |  |  |
| LastPurchaseDate | date | 3 | 1 |  |  |  |
| LastPurchaseChan | date | 3 | 1 |  |  |  |
| PreferredStory | varchar | 100 | 1 |  |  |  |
| SubscriberID | int | 4 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
| StoreName | varchar | 100 | 1 |  |  |  |
