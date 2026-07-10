# dbo.tmpDataLakeVsDynDiscounts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Entity | varchar | 4 | 1 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| InventLocationId | varchar | 4 | 1 |  |  |  |
| DataLakeRetailTransactionId | nvarchar | 88 | 1 |  |  |  |
| DataLakeAmount | numeric | 9 | 1 |  |  |  |
| DatalakeDiscountOriginType | nvarchar | 16 | 1 |  |  |  |
| DataLakePeriodicDiscountOfferId | nvarchar | 40 | 1 |  |  |  |
| RetailTransactionId | varchar | 44 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| DiscountOriginType | varchar | 10 | 1 |  |  |  |
| PeriodicDiscountOfferId | varchar | 20 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| CurrentSentDate | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
