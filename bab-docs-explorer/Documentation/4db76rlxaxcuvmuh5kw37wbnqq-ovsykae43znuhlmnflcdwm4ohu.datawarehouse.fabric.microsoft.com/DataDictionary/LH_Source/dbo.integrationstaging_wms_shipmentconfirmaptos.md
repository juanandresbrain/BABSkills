# dbo.integrationstaging_wms_shipmentconfirmaptos

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AptosShipmentID | varchar | 8000 | 1 |  |  |  |
| ModeOfDelivery | varchar | 8000 | 1 |  |  |  |
| ShipConfirmDateTime | varchar | 8000 | 1 |  |  |  |
| Warehouse | varchar | 8000 | 1 |  |  |  |
| ContainerID | varchar | 8000 | 1 |  |  |  |
| AptosDistributionNumber | bigint | 8 | 1 |  |  |  |
| AptosDistributionDocLineNumber | float | 8 | 1 |  |  |  |
| ContainerUnitOfMeasure | varchar | 8000 | 1 |  |  |  |
| ContainerUnitsShipped | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 8000 | 1 |  |  |  |
| OrderedQuantity | float | 8 | 1 |  |  |  |
| OrderedUnitOfMeasure | varchar | 8000 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| ShippedQuantity | int | 4 | 1 |  |  |  |
| ShippedUnitOfMeasure | varchar | 8000 | 1 |  |  |  |
| ToLocation | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| SentToPipelineDate | datetime2 | 8 | 1 |  |  |  |
| ContainerManifestID | varchar | 8000 | 1 |  |  |  |
