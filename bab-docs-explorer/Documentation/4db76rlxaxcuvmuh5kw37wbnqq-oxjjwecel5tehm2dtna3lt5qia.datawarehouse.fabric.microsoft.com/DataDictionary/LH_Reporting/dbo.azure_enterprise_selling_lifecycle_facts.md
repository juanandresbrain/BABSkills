# dbo.azure_enterprise_selling_lifecycle_facts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReferenceNumber | varchar | 8000 | 1 |  |  |  |
| ESOrderStatus | varchar | 8000 | 1 |  |  |  |
| OrderTransactionID | decimal | 9 | 1 |  |  |  |
| LineSeq | decimal | 5 | 1 |  |  |  |
| OrderStoreKey | int | 4 | 1 |  |  |  |
| OrderStoreNumber | varchar | 8000 | 1 |  |  |  |
| OrderTransactionDate | date | 3 | 1 |  |  |  |
| HasNonESItems | varchar | 8000 | 1 |  |  |  |
| ProductKey | int | 4 | 1 |  |  |  |
| OrderUnits | bigint | 8 | 1 |  |  |  |
| OrderAmount | decimal | 13 | 1 |  |  |  |
| FulfillTransactionID | decimal | 9 | 1 |  |  |  |
| FulfillmentStoreKey | int | 4 | 1 |  |  |  |
| FulfillStoreNumber | varchar | 8000 | 1 |  |  |  |
| FulfillTransactionDate | date | 3 | 1 |  |  |  |
| FulfillUnits | bigint | 8 | 1 |  |  |  |
| FulfillAmount | decimal | 13 | 1 |  |  |  |
| CancelTransactionID | decimal | 9 | 1 |  |  |  |
| CancelTransactionDate | date | 3 | 1 |  |  |  |
| CancelUnits | bigint | 8 | 1 |  |  |  |
| CancelAmount | decimal | 13 | 1 |  |  |  |
| ReturnTransactionID | decimal | 9 | 1 |  |  |  |
| ReturnTransactionDate | date | 3 | 1 |  |  |  |
| ReturnUnits | bigint | 8 | 1 |  |  |  |
| ReturnAmount | decimal | 13 | 1 |  |  |  |
| ESFulfillmentDuration | bigint | 8 | 1 |  |  |  |
| FulfillMentStoreName | varchar | 8000 | 1 |  |  |  |
| FulfillMentStroreArea | varchar | 8000 | 1 |  |  |  |
| FulfillmentStoreZone | varchar | 8000 | 1 |  |  |  |
