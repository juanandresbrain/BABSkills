# dbo.integrationstaging_wms_salesorderstatusupdateshipped

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveId | varchar | 8000 | 1 |  |  |  |
| ModeOfDelivery | varchar | 8000 | 1 |  |  |  |
| ShipConfirmDateTime | datetime2 | 8 | 1 |  |  |  |
| Warehouse | varchar | 8000 | 1 |  |  |  |
| ShipmentId | varchar | 8000 | 1 |  |  |  |
| ShipmentStatus | varchar | 8000 | 1 |  |  |  |
| ContainerId | varchar | 8000 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 8000 | 1 |  |  |  |
| ItemId | varchar | 8000 | 1 |  |  |  |
| SalesPoolId | varchar | 8000 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| DeckSalesOrderReferenceNumber | varchar | 8000 | 1 |  |  |  |
| ShippedQty | int | 4 | 1 |  |  |  |
