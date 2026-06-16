# WEB.DynamicActionOrderLinesStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderID | varchar | 50 | 1 |  |  |  |
| PlacedTimestamp | date | 3 | 1 |  |  |  |
| SKU | varchar | 100 | 1 |  |  |  |
| ProductID | varchar | 100 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 10 | 1 |  |  |  |
| Sales | numeric | 5 | 1 |  |  |  |
| SalesExTax | numeric | 5 | 1 |  |  |  |
| PromoInfo | varchar | 1000 | 1 |  |  |  |
| ShippingAmount | numeric | 5 | 1 |  |  |  |
| ShippingExTax | numeric | 5 | 1 |  |  |  |
| ShippingCost | numeric | 5 | 1 |  |  |  |
| ShippingMethod | varchar | 20 | 1 |  |  |  |
| Site | varchar | 10 | 1 |  |  |  |
| OrderItemGrouping | int | 4 | 1 |  |  |  |

