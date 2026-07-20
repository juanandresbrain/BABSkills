# dbo.azure_web_order_inbound_integration_tracking

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ExposedDate | date | 3 | 1 |  |  |  |
| ExposedOrderNumber | varchar | 8000 | 1 |  |  |  |
| isRecordYourVoice | int | 4 | 1 |  |  |  |
| isRecorded | int | 4 | 1 |  |  |  |
| isWaitingOnRecordYourVoice | int | 4 | 1 |  |  |  |
| DeckOrderNumber | varchar | 8000 | 1 |  |  |  |
| DeckOrderNetTotal | decimal | 17 | 1 |  |  |  |
| DeckOrderDate | date | 3 | 1 |  |  |  |
| ImportedOrderNumber | varchar | 8000 | 1 |  |  |  |
| ImportedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| ImportedDate | date | 3 | 1 |  |  |  |
| WOPOrderNumber | varchar | 8000 | 1 |  |  |  |
| WOPWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| WOPCountry | varchar | 8000 | 1 |  |  |  |
| WOPFulfillmentLocation | varchar | 8000 | 1 |  |  |  |
| WOPNewOrderStatusDate | date | 3 | 1 |  |  |  |
| DynamicsAPIOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPIWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPISalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsAPILogDate | date | 3 | 1 |  |  |  |
| DynamicsSalesOrderNumber | varchar | 8000 | 1 |  |  |  |
| DynamicsOrderCreationDateTime | date | 3 | 1 |  |  |  |
| UKFTPOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKFTPWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKFTPLogDate | date | 3 | 1 |  |  |  |
| UKCreatedOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKCreatedWebOrderNumber | varchar | 8000 | 1 |  |  |  |
| UKCreatedLogDate | date | 3 | 1 |  |  |  |
| isDeckFiled | int | 4 | 1 |  |  |  |
| isImported | int | 4 | 1 |  |  |  |
| isWebOrderProcessing | int | 4 | 1 |  |  |  |
| isDynamicsAPI | int | 4 | 1 |  |  |  |
| isDynamicsWMS | int | 4 | 1 |  |  |  |
| isUKFTP | int | 4 | 1 |  |  |  |
| isUKCreated | int | 4 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isWeb | int | 4 | 1 |  |  |  |
| isStore | int | 4 | 1 |  |  |  |
| isUSWeb | int | 4 | 1 |  |  |  |
| isUSStore | int | 4 | 1 |  |  |  |
| isUKWeb | int | 4 | 1 |  |  |  |
| isUKStore | int | 4 | 1 |  |  |  |
| isMissingInDeckFile | int | 4 | 1 |  |  |  |
| isMissingInImportLog | int | 4 | 1 |  |  |  |
| isMissingInWebOrderProcessing | int | 4 | 1 |  |  |  |
| isMissingDynamicsAPI | int | 4 | 1 |  |  |  |
| isMissingInDynamics | int | 4 | 1 |  |  |  |
| isMissingInUKFTP | int | 4 | 1 |  |  |  |
| isMissingInUKwms | int | 4 | 1 |  |  |  |
