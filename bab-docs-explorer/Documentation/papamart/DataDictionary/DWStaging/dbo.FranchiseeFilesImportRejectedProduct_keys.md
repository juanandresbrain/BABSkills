# dbo.FranchiseeFilesImportRejectedProduct_keys

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | varchar | 20 | 1 |  |  |  |
| Style | varchar | 6 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| Cost | numeric | 5 | 1 |  |  |  |
| GrossSales | numeric | 5 | 1 |  |  |  |
| Discount | numeric | 5 | 1 |  |  |  |
| VAT | numeric | 5 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| FranchiseeTransactionHeaderID | int | 4 | 1 |  |  |  |
| FranchiseeTransactionMerchandiseID | bigint | 8 | 1 |  |  |  |
| Franchisee | varchar | 2 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
