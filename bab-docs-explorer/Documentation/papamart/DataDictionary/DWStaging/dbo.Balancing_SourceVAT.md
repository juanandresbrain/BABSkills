# dbo.Balancing_SourceVAT

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | datetime | 8 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_id | int | 4 | 0 |  |  |  |
| VAT | numeric | 17 | 1 |  |  |  |
