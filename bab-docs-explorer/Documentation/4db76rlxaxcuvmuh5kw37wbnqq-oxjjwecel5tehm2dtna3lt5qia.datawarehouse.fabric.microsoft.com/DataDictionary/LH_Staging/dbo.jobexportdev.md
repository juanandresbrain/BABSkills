# dbo.jobexportdev

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobID | int | 4 | 1 |  |  |  |
| EmailID | int | 4 | 1 |  |  |  |
| AccountID | int | 4 | 1 |  |  |  |
| AccountUserID | int | 4 | 1 |  |  |  |
| FromName | varchar | 8000 | 1 |  |  |  |
| FromEmail | varchar | 8000 | 1 |  |  |  |
| SchedTime | datetime2 | 8 | 1 |  |  |  |
| PickupTime | datetime2 | 8 | 1 |  |  |  |
| DeliveredTime | datetime2 | 8 | 1 |  |  |  |
| EventID | varchar | 8000 | 1 |  |  |  |
| IsMultipart | bit | 1 | 1 |  |  |  |
| JobType | varchar | 8000 | 1 |  |  |  |
| JobStatus | varchar | 8000 | 1 |  |  |  |
| ModifiedBy | int | 4 | 1 |  |  |  |
| ModifiedDate | datetime2 | 8 | 1 |  |  |  |
| EmailName | varchar | 8000 | 1 |  |  |  |
| EmailSubject | varchar | 8000 | 1 |  |  |  |
| IsWrapped | bit | 1 | 1 |  |  |  |
| TestEmailAddr | varchar | 8000 | 1 |  |  |  |
| Category | varchar | 8000 | 1 |  |  |  |
| BccEmail | varchar | 8000 | 1 |  |  |  |
| OriginalSchedTime | varchar | 8000 | 1 |  |  |  |
| CreatedDate | datetime2 | 8 | 1 |  |  |  |
| CharacterSet | varchar | 8000 | 1 |  |  |  |
| IPAddress | varchar | 8000 | 1 |  |  |  |
| SalesForceTotalSubscriberCount | int | 4 | 1 |  |  |  |
| SalesForceErrorSubscriberCount | int | 4 | 1 |  |  |  |
| SendType | varchar | 8000 | 1 |  |  |  |
| DynamicEmailSubject | varchar | 8000 | 1 |  |  |  |
| SuppressTracking | bit | 1 | 1 |  |  |  |
| SendClassificationType | varchar | 8000 | 1 |  |  |  |
| SendClassification | varchar | 8000 | 1 |  |  |  |
| ResolveLinksWithCurrentData | bit | 1 | 1 |  |  |  |
| EmailSendDefinition | int | 4 | 1 |  |  |  |
| DeduplicateByEmail | bit | 1 | 1 |  |  |  |
| TriggererSendDefinitionObjectID | varchar | 8000 | 1 |  |  |  |
| TriggeredSendCustomerKey | varchar | 8000 | 1 |  |  |  |
