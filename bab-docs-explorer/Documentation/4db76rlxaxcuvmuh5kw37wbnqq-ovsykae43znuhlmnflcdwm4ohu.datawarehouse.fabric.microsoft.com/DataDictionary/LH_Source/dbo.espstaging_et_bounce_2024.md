# dbo.espstaging_et_bounce_2024

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| SubscriberID | int | 4 | 1 |  |  |  |
| ListID | int | 4 | 1 |  |  |  |
| EventDate | datetime2 | 8 | 1 |  |  |  |
| EventType | varchar | 8000 | 1 |  |  |  |
| BounceCategory | varchar | 8000 | 1 |  |  |  |
| SMTPCode | varchar | 8000 | 1 |  |  |  |
| BounceReason | varchar | 8000 | 1 |  |  |  |
| BatchID | int | 4 | 1 |  |  |  |
| TriggeredSendExternalKey | varchar | 8000 | 1 |  |  |  |
| Load_ID | int | 4 | 1 |  |  |  |
| ProcessDate | datetime2 | 8 | 1 |  |  |  |
