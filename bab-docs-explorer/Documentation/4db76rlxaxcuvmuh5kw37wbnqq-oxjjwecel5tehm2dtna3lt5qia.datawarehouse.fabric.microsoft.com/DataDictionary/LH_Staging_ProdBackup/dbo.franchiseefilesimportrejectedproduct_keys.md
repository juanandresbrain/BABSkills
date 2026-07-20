# dbo.franchiseefilesimportrejectedproduct_keys

**Database:** LH_Staging_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | varchar | 8000 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| Cost | decimal | 5 | 1 |  |  |  |
| GrossSales | decimal | 5 | 1 |  |  |  |
| Discount | decimal | 5 | 1 |  |  |  |
| VAT | decimal | 5 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| FranchiseeTransactionHeaderID | int | 4 | 1 |  |  |  |
| FranchiseeTransactionMerchandiseID | bigint | 8 | 1 |  |  |  |
| Franchisee | varchar | 8000 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
