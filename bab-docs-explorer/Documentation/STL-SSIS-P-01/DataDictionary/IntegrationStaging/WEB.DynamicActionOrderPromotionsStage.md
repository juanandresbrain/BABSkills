# WEB.DynamicActionOrderPromotionsStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| orderid | varchar | 50 | 1 |  |  |  |
| SKU | varchar | 50 | 1 |  |  |  |
| PromoCode | varchar | 40 | 1 |  |  |  |
| DiscountAmount | numeric | 5 | 1 |  |  |  |
| IsOrderLevelDiscount | bit | 1 | 1 |  |  |  |
| DiscountName | varchar | 50 | 1 |  |  |  |
| SourceSite | varchar | 10 | 1 |  |  |  |

