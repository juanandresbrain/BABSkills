# dbo.WebOrderDiscountsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderDate | date | 3 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| SKU | varchar | 50 | 1 |  |  |  |
| ItemDiscountAmount | numeric | 17 | 1 |  |  |  |
| OrderItemDiscountAmount | numeric | 17 | 1 |  |  |  |
| TotalDiscountAmount | numeric | 17 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
