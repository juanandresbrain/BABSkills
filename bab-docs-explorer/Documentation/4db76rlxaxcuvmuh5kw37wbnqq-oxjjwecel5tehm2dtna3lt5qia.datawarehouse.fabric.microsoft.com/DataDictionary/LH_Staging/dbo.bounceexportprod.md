# dbo.bounceexportprod

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AccountID | int | 4 | 1 |  |  |  |
| OYBAccountID | int | 4 | 1 |  |  |  |
| JobID | int | 4 | 1 |  |  |  |
| ListID | int | 4 | 1 |  |  |  |
| BatchID | int | 4 | 1 |  |  |  |
| SubscriberID | int | 4 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| EventDate | datetime2 | 8 | 1 |  |  |  |
| IsUnique | bit | 1 | 1 |  |  |  |
| Domain | varchar | 8000 | 1 |  |  |  |
| BounceCategoryID | int | 4 | 1 |  |  |  |
| BounceCategory | varchar | 8000 | 1 |  |  |  |
| BounceSubcategoryID | int | 4 | 1 |  |  |  |
| BounceSubcategory | varchar | 8000 | 1 |  |  |  |
| BounceTypeID | int | 4 | 1 |  |  |  |
| BounceType | varchar | 8000 | 1 |  |  |  |
| SMTPBounceReason | varchar | 8000 | 1 |  |  |  |
| SMTPMessage | varchar | 8000 | 1 |  |  |  |
| SMTPCode | varchar | 8000 | 1 |  |  |  |
| TriggererSendDefinitionObjectID | varchar | 8000 | 1 |  |  |  |
| TriggeredSendCustomerKey | varchar | 8000 | 1 |  |  |  |
