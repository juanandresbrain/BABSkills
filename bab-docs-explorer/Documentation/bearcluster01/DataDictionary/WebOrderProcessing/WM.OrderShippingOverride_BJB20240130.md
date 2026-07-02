# WM.OrderShippingOverride_BJB20240130

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderShippingOverrideID | int | 4 | 0 |  |  |  |
| OverrideDescription | varchar | -1 | 0 |  |  |  |
| StateProvince | varchar | 2 | 1 |  |  |  |
| OriginalShipmentMethod | varchar | 20 | 0 |  |  |  |
| OverrideShipmentMethod | varchar | 20 | 0 |  |  |  |
| StartDateTime | datetime | 8 | 0 |  |  |  |
| EndDateTime | datetime | 8 | 0 |  |  |  |
| CreatedBy | varchar | 255 | 0 |  |  |  |
| CreatedOn | datetime | 8 | 0 |  |  |  |
| UpdatedBy | varchar | 255 | 1 |  |  |  |
| UpdatedOn | datetime | 8 | 1 |  |  |  |
| Country | varchar | 255 | 1 |  |  |  |

