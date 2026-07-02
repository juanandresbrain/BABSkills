# WEB.BundleSalePriceFact

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UnionSource | varchar | 6 | 1 |  |  |  |
| BundleSku | varchar | 150 | 1 |  |  |  |
| BundleSkuCatalog | varchar | 2 | 1 |  |  |  |
| SalePriceStartDateTime | datetime | 8 | 1 |  |  |  |
| SalePriceEndDateTime | datetime | 8 | 1 |  |  |  |
| BundSkuSalePrice | numeric | 17 | 1 |  |  |  |
| BundleSkuListPrice | numeric | 9 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

