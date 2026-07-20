# dbo.retailinventoryloadandvolumedatastaging

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| SalesTransactionsHeader | int | 4 | 1 |  |  |  |
| SalesTransactionsLine | int | 4 | 1 |  |  |  |
| Taxlines | int | 4 | 1 |  |  |  |
| TenderLines | int | 4 | 1 |  |  |  |
| DiscountLines | int | 4 | 1 |  |  |  |
