# WEB.BundleSalePriceStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Sku | varchar | 50 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| Retail | decimal | 9 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| StartTime | time | 5 | 1 |  |  |  |
| EndDate | date | 3 | 1 |  |  |  |
| EndTime | time | 5 | 1 |  |  |  |
| Reference | varchar | 100 | 1 |  |  |  |
| Catalog | varchar | 2 | 1 |  |  |  |
| DerivedStyleCode | varchar | 50 | 1 |  |  |  |
| DerivedStartDateTime | datetime | 8 | 1 |  |  |  |
| DerivedEndDateTime | datetime | 8 | 1 |  |  |  |

