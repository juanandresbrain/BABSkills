# dbo.#BC35BFD7

**Database:** tempdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SalesOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| SalesOrderStatus | nvarchar | 100 | 1 |  |  |  |
| SalesOrderProcessingStatus | nvarchar | 510 | 1 |  |  |  |
| SalesOrderOriginCode | nvarchar | 8000 | 1 |  |  |  |
| SalesOrderPoolId | nvarchar | 8000 | 1 |  |  |  |
| ShippingCarrierId | nvarchar | 8000 | 1 |  |  |  |
| ShippingCarrierServiceId | nvarchar | 8000 | 1 |  |  |  |
| OrderCreationDateTime | datetime | 8 | 1 |  |  |  |
| DeliveryModeCode | nvarchar | 8000 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| OrderedSalesQuantity | float | 8 | 1 |  |  |  |
| LineDescription | nvarchar | 8000 | 1 |  |  |  |
| WebOrderNumber | nvarchar | 20 | 1 |  |  |  |
| WaveID | varchar | 25 | 1 |  |  |  |
| ReleasedDateAndTime | datetime | 8 | 1 |  |  |  |
| ContainerID | varchar | 20 | 1 |  |  |  |
| WorkID | varchar | 20 | 1 |  |  |  |
| DeckOrderDate | datetime | 8 | 1 |  |  |  |
| DynamicsOrderAge | int | 4 | 1 |  |  |  |
| isWaved | int | 4 | 0 |  |  |  |
| isIntl | int | 4 | 0 |  |  |  |
| isRyv | int | 4 | 0 |  |  |  |
| isEmb | int | 4 | 0 |  |  |  |
| ProcessingAge | int | 4 | 1 |  |  |  |
| isShippedOrCancelledInDeck | int | 4 | 1 |  |  |  |

