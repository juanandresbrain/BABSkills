# dbo.subscriberexportdev

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SubscriberID | int | 4 | 1 |  |  |  |
| DateUndeliverable | varchar | 8000 | 1 |  |  |  |
| DateJoined | datetime2 | 8 | 1 |  |  |  |
| DateUnsubscribed | datetime2 | 8 | 1 |  |  |  |
| Domain | varchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| BounceCount | int | 4 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| SubscriberType | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
