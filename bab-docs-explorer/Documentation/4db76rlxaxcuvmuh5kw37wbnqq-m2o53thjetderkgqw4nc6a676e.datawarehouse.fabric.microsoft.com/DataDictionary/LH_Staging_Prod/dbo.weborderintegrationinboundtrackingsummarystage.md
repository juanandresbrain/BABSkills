# dbo.weborderintegrationinboundtrackingsummarystage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
