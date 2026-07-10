# dbo.EmlRevStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendID | int | 4 | 1 |  |  |  |
| EmailAddress | varchar | 50 | 1 |  |  |  |
| FrequencyCount1m | int | 4 | 1 |  |  |  |
| FrequencyCount3m | int | 4 | 1 |  |  |  |
| FrequencyCount6m | int | 4 | 1 |  |  |  |
| FrequencyCount12m | int | 4 | 1 |  |  |  |
| FrequencyCount18m | int | 4 | 1 |  |  |  |
| FrequencyCountTTL | int | 4 | 1 |  |  |  |
| RecencyCount1m | int | 4 | 1 |  |  |  |
| RecencyCount3m | int | 4 | 1 |  |  |  |
| RecencyCount6m | int | 4 | 1 |  |  |  |
| RecencyCount12m | int | 4 | 1 |  |  |  |
| RecencyCountTTL | int | 4 | 1 |  |  |  |
| MonetarySum1m | numeric | 9 | 1 |  |  |  |
| MonetarySum6m | numeric | 9 | 1 |  |  |  |
| MonetarySumTTL | numeric | 9 | 1 |  |  |  |
| LastTransactionDate | varchar | 50 | 1 |  |  |  |
| LastTransactionStore | varchar | 50 | 1 |  |  |  |
