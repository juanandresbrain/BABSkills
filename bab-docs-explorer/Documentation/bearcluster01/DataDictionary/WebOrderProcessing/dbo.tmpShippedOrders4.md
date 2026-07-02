# dbo.tmpShippedOrders4

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderNumber | varchar | 10 | 1 |  |  |  |
| OrderDate | datetime | 8 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
| ShippingAmount | money | 8 | 1 |  |  |  |
| PreviousShipping | money | 8 | 1 |  |  |  |
| LoyaltyNumber | varchar | 64 | 1 |  |  |  |
| PickupStore | varchar | 4 | 1 |  |  |  |

