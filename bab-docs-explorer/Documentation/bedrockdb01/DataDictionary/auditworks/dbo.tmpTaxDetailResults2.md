# dbo.tmpTaxDetailResults2

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerCode | int | 4 | 1 |  |  |  |
| DocCode | varchar | 50 | 1 |  |  |  |
| transaction_date | varchar | 50 | 1 |  |  |  |
| CompanyCode | varchar | 50 | 1 |  |  |  |
| TaxCode | varchar | 50 | 1 |  |  |  |
| TaxDate | varchar | 50 | 1 |  |  |  |
| Amount | numeric | 17 | 1 |  |  |  |
| Ref1 | varchar | 50 | 1 |  |  |  |
| Ref2 | int | 4 | 1 |  |  |  |
| line_id | int | 4 | 1 |  |  |  |
| CurrencyCode | varchar | 50 | 1 |  |  |  |
| TotalTax | numeric | 17 | 1 |  |  |  |
| DestAddress | varchar | 150 | 1 |  |  |  |
| DestCity | varchar | 50 | 1 |  |  |  |
| DestRegion | varchar | 50 | 1 |  |  |  |
| DestPostalCode | varchar | 50 | 1 |  |  |  |
| DestCountry | varchar | 50 | 1 |  |  |  |
| OrigRegion | varchar | 50 | 1 |  |  |  |
| OrigPostalCode | varchar | 50 | 1 |  |  |  |
