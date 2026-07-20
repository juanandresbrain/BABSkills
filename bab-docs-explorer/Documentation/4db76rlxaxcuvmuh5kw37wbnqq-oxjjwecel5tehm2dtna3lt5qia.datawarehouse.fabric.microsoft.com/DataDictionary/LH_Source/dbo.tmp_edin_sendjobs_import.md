# dbo.tmp_edin_sendjobs_import

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| FromName | varchar | 8000 | 1 |  |  |  |
| FromEmail | varchar | 8000 | 1 |  |  |  |
| SchedTime | datetime2 | 8 | 1 |  |  |  |
| SentTime | datetime2 | 8 | 1 |  |  |  |
| Subject | varchar | 8000 | 1 |  |  |  |
| EmailName | varchar | 8000 | 1 |  |  |  |
| TriggeredSendExternalKey | varchar | 8000 | 1 |  |  |  |
| SendDefinitionExternalKey | varchar | 8000 | 1 |  |  |  |
| JobStatus | varchar | 8000 | 1 |  |  |  |
| PreviewURL | varchar | 8000 | 1 |  |  |  |
| IsMultipart | varchar | 8000 | 1 |  |  |  |
| Additional | varchar | 8000 | 1 |  |  |  |
