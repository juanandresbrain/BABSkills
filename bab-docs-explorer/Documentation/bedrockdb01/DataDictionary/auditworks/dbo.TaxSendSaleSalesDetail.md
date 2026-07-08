# dbo.TaxSendSaleSalesDetail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerCode | int | 4 | 1 |  |  |  |
| DocCode | varchar | 12 | 1 |  |  |  |
| transaction_date | char | 30 | 1 |  |  |  |
| CompanyCode | varchar | 6 | 1 |  |  |  |
| TaxCode | nvarchar | 100 | 1 |  |  |  |
| TaxDate | char | 30 | 1 |  |  |  |
| Amount | numeric | 17 | 1 |  |  |  |
| Ref1 | nchar | 10 | 1 |  |  |  |
| Ref2 | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| CurrencyCode | nvarchar | 6 | 1 |  |  |  |
| TotalTax | numeric | 13 | 1 |  |  |  |
| DestAddress | nvarchar | 80 | 1 |  |  |  |
| DestCity | nvarchar | 80 | 1 |  |  |  |
| DestRegion | nvarchar | 4 | 1 |  |  |  |
| DestPostalCode | nvarchar | 40 | 1 |  |  |  |
| DestCountry | nvarchar | 80 | 1 |  |  |  |
| OrigRegion | nvarchar | 6 | 1 |  |  |  |
| OrigPostalCode | varchar | 10 | 1 |  |  |  |
