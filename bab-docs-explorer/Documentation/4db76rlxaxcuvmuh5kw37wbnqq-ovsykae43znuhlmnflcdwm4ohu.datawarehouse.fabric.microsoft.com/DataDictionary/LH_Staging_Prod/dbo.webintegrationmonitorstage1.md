# dbo.webintegrationmonitorstage1

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ImportedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| ImportedDate | date | 3 | 1 |  |  |  |
| DeckOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckOrderNetTotal | decimal | 9 | 1 |  |  |  |
| DeckOrderDate | date | 3 | 1 |  |  |  |
| ImportedOrderNumber | varchar | 8000 | 1 |  |  |  |
| isDeckRecordYourVoice | int | 4 | 1 |  |  |  |
| isDeckRecorded | int | 4 | 1 |  |  |  |
| ExposedOrderDeckVImported | varchar | 8000 | 1 |  |  |  |
