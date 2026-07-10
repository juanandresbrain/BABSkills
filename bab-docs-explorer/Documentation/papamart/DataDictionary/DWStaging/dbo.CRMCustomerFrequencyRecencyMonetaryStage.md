# dbo.CRMCustomerFrequencyRecencyMonetaryStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| LifetimeTransactionCount | int | 4 | 1 |  |  |  |
| LifetimeRecencyCount | int | 4 | 1 |  |  |  |
| LifetimeSalesTotal | numeric | 17 | 1 |  |  |  |
| FirstStoreConcept | nvarchar | 12 | 1 |  |  |  |
| FirstTransactionDate | date | 3 | 1 |  |  |  |
| Frequency3M | int | 4 | 1 |  |  |  |
| Recency3M | int | 4 | 1 |  |  |  |
| Sales3M | numeric | 17 | 1 |  |  |  |
| minDaysBetween3M | int | 4 | 1 |  |  |  |
| maxDaysBetween3M | int | 4 | 1 |  |  |  |
| DaysBetween3M | int | 4 | 1 |  |  |  |
| Frequency6M | int | 4 | 1 |  |  |  |
| Recency6M | int | 4 | 1 |  |  |  |
| Sales6M | numeric | 17 | 1 |  |  |  |
| minDaysBetween6M | int | 4 | 1 |  |  |  |
| maxDaysBetween6M | int | 4 | 1 |  |  |  |
| DaysBetween6M | int | 4 | 1 |  |  |  |
| Frequency12M | int | 4 | 1 |  |  |  |
| Recency12M | int | 4 | 1 |  |  |  |
| Sales12M | numeric | 17 | 1 |  |  |  |
| minDaysBetween12M | int | 4 | 1 |  |  |  |
| maxDaysBetween12M | int | 4 | 1 |  |  |  |
| DaysBetween12M | int | 4 | 1 |  |  |  |
| Frequency18M | int | 4 | 1 |  |  |  |
| Recency18M | int | 4 | 1 |  |  |  |
| Sales18M | numeric | 17 | 1 |  |  |  |
| minDaysBetween18M | int | 4 | 1 |  |  |  |
| maxDaysBetween18M | int | 4 | 1 |  |  |  |
| DaysBetween18M | int | 4 | 1 |  |  |  |
| Frequency24M | int | 4 | 1 |  |  |  |
| Recency24M | int | 4 | 1 |  |  |  |
| Sales24M | numeric | 17 | 1 |  |  |  |
| minDaysBetween24M | int | 4 | 1 |  |  |  |
| maxDaysBetween24M | int | 4 | 1 |  |  |  |
| DaysBetween24M | int | 4 | 1 |  |  |  |
| Frequency1M | int | 4 | 1 |  |  |  |
| Recency1M | int | 4 | 1 |  |  |  |
| Sales1M | int | 4 | 1 |  |  |  |
| minDaysBetween1M | int | 4 | 1 |  |  |  |
| maxDaysBetween1M | int | 4 | 1 |  |  |  |
| DaysBetween1M | int | 4 | 1 |  |  |  |
| LastTransactionDate | date | 3 | 1 |  |  |  |
| LastTransactionStore | nvarchar | 40 | 1 |  |  |  |
| Frequency36M | int | 4 | 1 |  |  |  |
| Recency36M | int | 4 | 1 |  |  |  |
| Sales36M | numeric | 17 | 1 |  |  |  |
| minDaysBetween36M | int | 4 | 1 |  |  |  |
| maxDaysBetween36M | int | 4 | 1 |  |  |  |
| DaysBetween36M | int | 4 | 1 |  |  |  |
