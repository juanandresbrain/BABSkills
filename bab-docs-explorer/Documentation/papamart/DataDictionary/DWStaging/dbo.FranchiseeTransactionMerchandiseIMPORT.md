# dbo.FranchiseeTransactionMerchandiseIMPORT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | varchar | 20 | 0 |  |  |  |
| Style | varchar | 6 | 0 |  |  |  |
| Units | int | 4 | 0 |  |  |  |
| Cost | numeric | 5 | 0 |  |  |  |
| GrossSales | numeric | 5 | 0 |  |  |  |
| Discount | numeric | 5 | 0 |  |  |  |
| VAT | numeric | 5 | 0 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| Franchisee | varchar | 2 | 0 |  |  |  |
| OriginalDiscount | numeric | 5 | 1 |  |  |  |
