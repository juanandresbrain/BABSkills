# dbo.FranchiseeTransactionMerchandise

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FranchiseeTransactionHeaderID | int | 4 | 0 |  |  |  |
| FranchiseeTransactionMerchandiseID | int | 4 | 0 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| Units | int | 4 | 0 |  |  |  |
| Cost | numeric | 5 | 0 |  |  |  |
| GrossSales | numeric | 5 | 0 |  |  |  |
| Discount | numeric | 5 | 0 |  |  |  |
| VAT | numeric | 5 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| BatchID | varchar | 52 | 0 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| updateDate | datetime | 8 | 1 |  |  |  |
| OriginalDiscount | numeric | 5 | 1 |  |  |  |
