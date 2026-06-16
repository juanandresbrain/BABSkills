# WEB.DynamicActionSellingInventoryLocationStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Date | date | 3 | 1 |  |  |  |
| Site | varchar | 10 | 1 |  |  |  |
| ProductID | varchar | 12 | 1 |  |  |  |
| SKU | varchar | 12 | 1 |  |  |  |
| PublishDate | date | 3 | 1 |  |  |  |
| IsMarkdown | varchar | 1 | 1 |  |  |  |
| IsDiscontinued | varchar | 1 | 1 |  |  |  |
| isCore | varchar | 1 | 1 |  |  |  |
| SeasonStartDate | date | 3 | 1 |  |  |  |
| SeasonEndDate | date | 3 | 1 |  |  |  |
| IsSellable | varchar | 1 | 1 |  |  |  |
| IsBackOrder | varchar | 1 | 1 |  |  |  |
| IsPreOder | varchar | 1 | 1 |  |  |  |
| CurrentPrice | numeric | 9 | 1 |  |  |  |
| CurrentPriceExTax | numeric | 5 | 1 |  |  |  |
| FullPrice | numeric | 9 | 1 |  |  |  |
| FullPriceExTax | numeric | 5 | 1 |  |  |  |
| BackorderUnits | int | 4 | 1 |  |  |  |
| Pre-OrderUnits | int | 4 | 1 |  |  |  |
| WaitlistUnits | int | 4 | 1 |  |  |  |

