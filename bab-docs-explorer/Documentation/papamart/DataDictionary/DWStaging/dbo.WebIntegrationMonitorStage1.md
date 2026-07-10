# dbo.WebIntegrationMonitorStage1

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ImportedWebOrderNumber | varchar | 10 | 1 |  |  |  |
| ImportedDate | date | 3 | 1 |  |  |  |
| DeckOrderNumber | varchar | 50 | 1 |  |  |  |
| DeckOrderNetTotal | numeric | 9 | 1 |  |  |  |
| DeckOrderDate | date | 3 | 1 |  |  |  |
| ImportedOrderNumber | varchar | 8 | 1 |  |  |  |
| isDeckRecordYourVoice | int | 4 | 1 |  |  |  |
| isDeckRecorded | int | 4 | 1 |  |  |  |
| ExposedOrderDeckVImported | nvarchar | 16 | 1 |  |  |  |
