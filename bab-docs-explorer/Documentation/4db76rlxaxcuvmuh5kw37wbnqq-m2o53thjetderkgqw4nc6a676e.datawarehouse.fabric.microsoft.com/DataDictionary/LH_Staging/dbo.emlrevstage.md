# dbo.emlrevstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendID | int | 4 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
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
| MonetarySum1m | decimal | 9 | 1 |  |  |  |
| MonetarySum6m | decimal | 9 | 1 |  |  |  |
| MonetarySumTTL | decimal | 9 | 1 |  |  |  |
| LastTransactionDate | varchar | 8000 | 1 |  |  |  |
| LastTransactionStore | varchar | 8000 | 1 |  |  |  |
