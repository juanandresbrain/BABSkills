# ERP.validate_DistrosNotInDistroSplit

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | nvarchar | 8 | 1 |  |  |  |
| OrderType | varchar | 20 | 1 |  |  |  |
| OrderID | varchar | 20 | 1 |  |  |  |
| HeaderFromWhse | varchar | 5 | 1 |  |  |  |
| HeaderToWarehouse | varchar | 5 | 1 |  |  |  |
| HeaderShipToName | varchar | 100 | 1 |  |  |  |
| DetailLocation | varchar | 5 | 1 |  |  |  |
| DetailWarehouse | varchar | 5 | 1 |  |  |  |
| ModeOfDelivery | varchar | 10 | 1 |  |  |  |
| ItemNumber | varchar | 7 | 1 |  |  |  |
| Quantity | numeric | 17 | 1 |  |  |  |
| OrderCreateDate | datetime | 8 | 1 |  |  |  |
| OrderIntegrationDate | datetime | 8 | 1 |  |  |  |
| OrderReleasedToWhseDate | datetime | 8 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |
| DerivedModeOfDelivery | int | 4 | 1 |  |  |  |
| DerivedFromWarehouse | varchar | 10 | 1 |  |  |  |
| DerivedTOWAREHOUSE | varchar | 10 | 1 |  |  |  |
| DerivedQTY | int | 4 | 1 |  |  |  |
| HasItemMasterData | varchar | 3 | 1 |  |  |  |
| HasItemUOMData | varchar | 3 | 1 |  |  |  |
| HasProductData | varchar | 3 | 1 |  |  |  |
| DerivedStyleCode | varchar | 6 | 1 |  |  |  |

