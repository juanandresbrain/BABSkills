# dbo.tmpAWTaxDetailResultsFinal

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerCode | int | 4 | 1 |  |  |  |
| DocCode | varchar | 12 | 1 |  |  |  |
| transaction_date | char | 30 | 1 |  |  |  |
| CompanyCode | varchar | 6 | 1 |  |  |  |
| TaxCode | nvarchar | 100 | 1 |  |  |  |
| TaxDate | char | 30 | 1 |  |  |  |
| Amount | numeric | 9 | 1 |  |  |  |
| Ref1 | nchar | 10 | 1 |  |  |  |
| Ref2 | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| CurrencyCode | nchar | 6 | 1 |  |  |  |
| TotalTax | numeric | 13 | 1 |  |  |  |
| DestAddress | nvarchar | 200 | 1 |  |  |  |
| DestCity | nvarchar | 120 | 1 |  |  |  |
| DestRegion | nvarchar | 4 | 1 |  |  |  |
| DestPostalCode | nvarchar | 30 | 1 |  |  |  |
| DestCountry | nvarchar | 6 | 1 |  |  |  |
| OrigRegion | nchar | 6 | 1 |  |  |  |
| OrigPostalCode | varchar | 10 | 1 |  |  |  |
