# dbo.EmailBounceStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SubscriberKey | varchar | 200 | 1 |  |  |  |
| EmailAddress | varchar | 200 | 1 |  |  |  |
| BounceDate | datetime | 8 | 1 |  |  |  |
