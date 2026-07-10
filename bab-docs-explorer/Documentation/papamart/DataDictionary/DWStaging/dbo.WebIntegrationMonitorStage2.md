# dbo.WebIntegrationMonitorStage2

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WOPOrderNumber | varchar | 10 | 1 |  |  |  |
| WOPWebOrderNumber | varchar | 10 | 1 |  |  |  |
| WOPCountry | varchar | 2 | 1 |  |  |  |
| WOPFulfillmentLocation | varchar | 4 | 1 |  |  |  |
| WOPNewOrderStatusDate | date | 3 | 1 |  |  |  |
| isWOPRecordYourVoice | int | 4 | 1 |  |  |  |
| isWOPRecorded | int | 4 | 1 |  |  |  |
