# dbo.WebOrderIntegrationInboundTracking

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TrackingIdentifier | int | 4 | 0 | YES |  |  |
| DeckOrderNumber | varchar | 50 | 1 |  |  |  |
| DeckCountry | varchar | 2 | 1 |  |  |  |
| DeckOrderNetTotal | numeric | 17 | 1 |  |  |  |
| DeckOrderDate | date | 3 | 1 |  |  |  |
| ImportedOrderNumber | varchar | 8 | 1 |  |  |  |
| ImportedWebOrderNumber | varchar | 10 | 1 |  |  |  |
| ImportedDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImported | nvarchar | 16 | 1 |  |  |  |
| WOPOrderNumber | varchar | 8 | 1 |  |  |  |
| WOPWebOrderNumber | varchar | 10 | 1 |  |  |  |
| WOPCountry | varchar | 2 | 1 |  |  |  |
| WOPFulfillmentLocation | varchar | 4 | 1 |  |  |  |
| WOPNewOrderStatusDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOP | nvarchar | 16 | 1 |  |  |  |
| DynamicsAPIOrderNumber | varchar | 8 | 1 |  |  |  |
| DynamicsAPIWebOrderNumber | varchar | 10 | 1 |  |  |  |
| DynamicsAPISalesOrderNumber | varchar | 20 | 1 |  |  |  |
| DynamicsAPILogDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOPVDynamicsAPI | nvarchar | 16 | 1 |  |  |  |
| DynamicsSalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| DynamicsOrderCreationDateTime | date | 3 | 1 |  |  |  |
| UKFTPOrderNumber | varchar | 8 | 1 |  |  |  |
| UKFTPWebOrderNumber | varchar | 10 | 1 |  |  |  |
| UKFTPLogDate | date | 3 | 1 |  |  |  |
| ExposedOrderDeckVImportedVWOPVUKFTP | nvarchar | 16 | 1 |  |  |  |
| UKCreatedOrderNumber | varchar | 8 | 1 |  |  |  |
| UKCreatedWebOrderNumber | varchar | 10 | 1 |  |  |  |
| UKCreatedLogDate | date | 3 | 1 |  |  |  |
| ExposedOrderUK | nvarchar | 16 | 1 |  |  |  |
| ExposedOrderNumber | nvarchar | 16 | 1 |  |  |  |
| isRecordYourVoice | int | 4 | 1 |  |  |  |
| isRecorded | int | 4 | 1 |  |  |  |
| Country | varchar | 2 | 1 |  |  |  |
