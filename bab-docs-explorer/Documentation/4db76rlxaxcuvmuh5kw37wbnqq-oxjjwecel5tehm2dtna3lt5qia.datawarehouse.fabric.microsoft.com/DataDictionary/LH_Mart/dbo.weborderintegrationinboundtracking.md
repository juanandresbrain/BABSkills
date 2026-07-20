# dbo.weborderintegrationinboundtracking

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TrackingIdentifier | int | 4 | 1 |  |  |  |
| DeckOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckCountry | varchar | 8000 | 1 |  |  |  |
| DeckOrderNetTotal | decimal | 17 | 1 |  |  |  |
| DeckOrderDate | date | 3 | 1 |  |  |  |
| ImportedOrderNumber | varchar | 8000 | 1 |  |  |  |
| ImportedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| ImportedDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImported | varchar | 8000 | 1 |  |  |  |
| WOPOrderNumber | varchar | 8000 | 1 |  |  |  |
| WOPWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| WOPCountry | varchar | 8000 | 1 |  |  |  |
| WOPFulfillmentLocation | varchar | 8000 | 1 |  |  |  |
| WOPNewOrderStatusDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOP | varchar | 8000 | 1 |  |  |  |
| DynamicsAPIOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPIWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPISalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPILogDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOPVDynamicsAPI | varchar | 8000 | 1 |  |  |  |
| DynamicsSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsOrderCreationDateTime | date | 3 | 1 |  |  |  |
| UKFTPOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKFTPWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKFTPLogDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOPVUKFTP | varchar | 8000 | 1 |  |  |  |
| UKCreatedOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKCreatedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKCreatedLogDate | date | 3 | 1 |  |  |  |
| ExposedOrderUK | varchar | 8000 | 1 |  |  |  |
| ExposedOrderNumber | varchar | 8000 | 1 |  |  |  |
| isRecordYourVoice | int | 4 | 1 |  |  |  |
| isRecorded | int | 4 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
