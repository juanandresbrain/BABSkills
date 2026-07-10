# dbo.RetailInventoryLoadAndVolumeDataStaging

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| date_key | int | 4 | 0 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| hour | int | 4 | 1 |  |  |  |
| SalesTransactionsHeader | int | 4 | 0 |  |  |  |
| SalesTransactionsLine | int | 4 | 0 |  |  |  |
| Taxlines | int | 4 | 0 |  |  |  |
| TenderLines | int | 4 | 0 |  |  |  |
| DiscountLines | int | 4 | 0 |  |  |  |
