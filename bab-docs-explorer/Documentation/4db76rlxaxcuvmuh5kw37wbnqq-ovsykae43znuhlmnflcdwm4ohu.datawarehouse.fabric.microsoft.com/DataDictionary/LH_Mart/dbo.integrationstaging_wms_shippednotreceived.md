# dbo.integrationstaging_wms_shippednotreceived

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| FromWarehouse | varchar | 8000 | 1 |  |  |  |
| ToWarehouse | varchar | 8000 | 1 |  |  |  |
| Receipt_Date | date | 3 | 1 |  |  |  |
| ModeOfDelivery | varchar | 8000 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 8000 | 1 |  |  |  |
| QuantityShipped | float | 8 | 1 |  |  |  |
| QuantityReceived | float | 8 | 1 |  |  |  |
| QuantityNotReceived | float | 8 | 1 |  |  |  |
| DistrictName | varchar | 8000 | 1 |  |  |  |
| DistrictManager | varchar | 8000 | 1 |  |  |  |
| DmId | int | 4 | 1 |  |  |  |
| DMfirstName | varchar | 8000 | 1 |  |  |  |
| DMlastName | varchar | 8000 | 1 |  |  |  |
| TMfirstName | varchar | 8000 | 1 |  |  |  |
| TMlastName | varchar | 8000 | 1 |  |  |  |
