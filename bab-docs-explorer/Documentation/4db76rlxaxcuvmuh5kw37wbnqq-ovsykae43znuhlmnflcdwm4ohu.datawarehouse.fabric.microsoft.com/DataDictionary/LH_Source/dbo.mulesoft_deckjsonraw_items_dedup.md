# dbo.mulesoft_deckjsonraw_items_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| OrderShipmentID | bigint | 8 | 1 |  |  |  |
| OrderShipmentItemID | bigint | 8 | 1 |  |  |  |
| OrderItemID | bigint | 8 | 1 |  |  |  |
| Tracking | varchar | 8000 | 1 |  |  |  |
| TrackingURI | varchar | 8000 | 1 |  |  |  |
| InternalItemStatusCode | varchar | 8000 | 1 |  |  |  |
| MarkForDeletion | bit | 1 | 1 |  |  |  |
| ShippingErrorID | bigint | 8 | 1 |  |  |  |
| DeliveredDateUTC | varchar | 8000 | 1 |  |  |  |
| ShippedDateUTC | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
