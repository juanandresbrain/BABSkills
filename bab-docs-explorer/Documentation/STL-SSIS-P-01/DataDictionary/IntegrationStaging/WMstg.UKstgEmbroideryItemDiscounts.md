# WMstg.UKstgEmbroideryItemDiscounts

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DiscountID | int | 4 | 1 |  |  |  |
| OrderItemID | int | 4 | 1 |  |  |  |
| PromoCode | varchar | 40 | 1 |  |  |  |
| DiscountAmount | money | 8 | 1 |  |  |  |
| IsOrderDiscount | bit | 1 | 1 |  |  |  |
| DiscountName | varchar | 50 | 1 |  |  |  |

