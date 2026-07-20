# dbo.tmp_edin_conversions_import

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
| ReferringURL | varchar | 8000 | 1 |  |  |  |
| LinkAlias | varchar | 8000 | 1 |  |  |  |
| ConversionData | varchar | 8000 | 1 |  |  |  |
| BatchID | int | 4 | 1 |  |  |  |
| TriggeredSendExternalKey | varchar | 8000 | 1 |  |  |  |
| URLID | int | 4 | 1 |  |  |  |
