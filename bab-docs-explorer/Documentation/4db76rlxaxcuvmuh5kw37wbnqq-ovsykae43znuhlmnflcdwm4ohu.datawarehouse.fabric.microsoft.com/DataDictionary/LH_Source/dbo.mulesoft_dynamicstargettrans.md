# dbo.mulesoft_dynamicstargettrans

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderId | bigint | 8 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| SiteCode | varchar | 8000 | 1 |  |  |  |
| MinWarehouseCode | varchar | 8000 | 1 |  |  |  |
| MaxWarehouseCode | varchar | 8000 | 1 |  |  |  |
| MaxShippingMethod | varchar | 8000 | 1 |  |  |  |
| OrderPoolId | varchar | 8000 | 1 |  |  |  |
| OrderStatus | bigint | 8 | 1 |  |  |  |
| OrderStatusCode | varchar | 8000 | 1 |  |  |  |
| OrderStatusDesc | varchar | 8000 | 1 |  |  |  |
| SubTotal | real | 4 | 1 |  |  |  |
| TotalNetTotal | real | 4 | 1 |  |  |  |
| Tax | real | 4 | 1 |  |  |  |
| Total | real | 4 | 1 |  |  |  |
| TotalGrossTotal | real | 4 | 1 |  |  |  |
| OrderDateUTC | datetime2 | 8 | 1 |  |  |  |
| OrderStatusChangeDateUTC | datetime2 | 8 | 1 |  |  |  |
| ExportCreatedUTC | datetime2 | 8 | 1 |  |  |  |
| DeliveryDate | datetime2 | 8 | 1 |  |  |  |
| SiteWarehouseCode | varchar | 8000 | 1 |  |  |  |
| ECommOrderType | varchar | 8000 | 1 |  |  |  |
