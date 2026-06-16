# WMS.TESTResponse

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _JSON | nvarchar | -1 | 1 |  |  |  |
| _RowIndex | int | 4 | 1 |  |  |  |
| swagger | nvarchar | 200 | 1 |  |  |  |
| info.description | nvarchar | 200 | 1 |  |  |  |
| info.version | nvarchar | 200 | 1 |  |  |  |
| info.title | nvarchar | 200 | 1 |  |  |  |
| paths./api/services/BABAptosServiceGroup/BABAptosInboundTOService/CreateTO.post.responses.200.description | nvarchar | 200 | 1 |  |  |  |
| paths./api/services/BABAptosServiceGroup/BABAptosInboundTOService/CreateTO.post.responses.200.schema.$ref | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.ShipDate.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.ReceiptDate.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.BABAptosShipmentNumber.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.DeliveryTerms.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.ModeOfDelivery.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.ToWarehouse.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOHeader.properties.FromWarehouse.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.ItemNumber.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.BABAptosDistroNumber.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.BABAptosDistroLineNumber.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.Quantity.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.UOM.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOLines.properties.InventoryStatus.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TransferOrder.properties.TOHeader.$ref | nvarchar | 200 | 1 |  |  |  |
| definitions.TransferOrder.properties.TOLines.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TransferOrder.properties.TOLines.items.$ref | nvarchar | 200 | 1 |  |  |  |
| definitions.TransferOrderReq.properties.TransferOrder.$ref | nvarchar | 200 | 1 |  |  |  |
| definitions.TOResponse.properties.$id.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOResponse.properties.TransferOrderId.type | nvarchar | 200 | 1 |  |  |  |
| definitions.TOResponse.properties.Created.type | nvarchar | 200 | 1 |  |  |  |
| _upstream.FromWarehouse | varchar | 4 | 1 |  |  |  |
| _upstream.ToWarehouse | varchar | 4 | 1 |  |  |  |
| _upstream.ModeOfDelivery | varchar | 52 | 1 |  |  |  |
| _upstream.DeliveryTerms | varchar | 100 | 1 |  |  |  |
| _upstream.ShipDate | date | 3 | 1 |  |  |  |
| _upstream.ReceiptDate | date | 3 | 1 |  |  |  |
| _upstream.ItemNumber | varchar | 7 | 1 |  |  |  |
| _upstream.InventoryStatus | varchar | 52 | 1 |  |  |  |
| _upstream.BABAptosShipmentNumber | varchar | 20 | 1 |  |  |  |
| _upstream.BABAptosDistroNumber | varchar | 20 | 1 |  |  |  |
| _upstream.BABBABAptosDistroNumber | int | 4 | 1 |  |  |  |
| _upstream.Quantity | int | 4 | 1 |  |  |  |
| _upstream.UOM | varchar | 20 | 1 |  |  |  |
| ContentType | nvarchar | 510 | 1 |  |  |  |
| ContentLength | numeric | 13 | 1 |  |  |  |
| HttpStatusCode | smallint | 2 | 1 |  |  |  |
| HttpResponseUrl | nvarchar | 4168 | 1 |  |  |  |
| HttpStatusCodeName | nvarchar | 510 | 1 |  |  |  |
| ResponseBody | nvarchar | -1 | 1 |  |  |  |

