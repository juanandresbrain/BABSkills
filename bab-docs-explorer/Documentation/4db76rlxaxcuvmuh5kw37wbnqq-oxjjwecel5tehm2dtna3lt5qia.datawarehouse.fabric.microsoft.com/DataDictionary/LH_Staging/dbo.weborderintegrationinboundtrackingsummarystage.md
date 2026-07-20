# dbo.weborderintegrationinboundtrackingsummarystage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActualDate | date | 3 | 1 |  |  |  |
| DeckOrdersCreated | int | 4 | 1 |  |  |  |
| US_WebOrders | int | 4 | 1 |  |  |  |
| US_StoreOrders | int | 4 | 1 |  |  |  |
| UK_WebOrders | int | 4 | 1 |  |  |  |
| UK_StoreOrders | int | 4 | 1 |  |  |  |
| DynamicsAPIWebOrders | int | 4 | 1 |  |  |  |
| DynamicsOrdersCreated | int | 4 | 1 |  |  |  |
| UKFTPOrders | int | 4 | 1 |  |  |  |
| UKCreatedOrders | int | 4 | 1 |  |  |  |
| ImportedOrders | int | 4 | 1 |  |  |  |
