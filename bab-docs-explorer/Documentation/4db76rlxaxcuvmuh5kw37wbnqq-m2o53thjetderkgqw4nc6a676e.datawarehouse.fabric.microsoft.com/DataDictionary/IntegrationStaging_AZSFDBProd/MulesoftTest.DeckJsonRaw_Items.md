# MulesoftTest.DeckJsonRaw_Items

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| OrderShipmentID | bigint | 8 | 1 |  |  |  |
| OrderShipmentItemID | bigint | 8 | 1 |  |  |  |
| OrderItemID | bigint | 8 | 1 |  |  |  |
| Tracking | varchar | -1 | 1 |  |  |  |
| TrackingURI | varchar | -1 | 1 |  |  |  |
| InternalItemStatusCode | varchar | -1 | 1 |  |  |  |
| MarkForDeletion | bit | 1 | 1 |  |  |  |
| ShippingErrorID | bigint | 8 | 1 |  |  |  |
| DeliveredDateUTC | varchar | -1 | 1 |  |  |  |
| ShippedDateUTC | varchar | -1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1881773761 | bigint | 8 | 0 |  |  |  |
