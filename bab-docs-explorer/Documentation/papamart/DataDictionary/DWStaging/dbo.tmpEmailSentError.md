# dbo.tmpEmailSentError

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| EmailAddress | varchar | 200 | 1 |  |  |  |
| SendDate | datetime | 8 | 1 |  |  |  |
| SubscriberKey | varchar | 200 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
