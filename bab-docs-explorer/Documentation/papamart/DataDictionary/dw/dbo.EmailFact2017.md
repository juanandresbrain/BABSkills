# dbo.EmailFact2017

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SubscriberKey | int | 4 | 1 |  |  |  |
| SendDate | datetime | 8 | 1 |  |  |  |
| EmailAddress | varchar | 200 | 1 |  |  |  |
| BounceDate | datetime | 8 | 1 |  |  |  |
| ClickDate | datetime | 8 | 1 |  |  |  |
| UnSubDate | datetime | 8 | 1 |  |  |  |
| OpenDate | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
