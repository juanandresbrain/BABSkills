# dbo.avalara_tax_trans

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProcessCode | int | 4 | 0 |  |  |  |
| DocCode | nvarchar | 100 | 0 |  |  |  |
| DocType | int | 4 | 0 |  |  |  |
| DocDate | smalldatetime | 4 | 0 |  |  |  |
| CompanyCode | nvarchar | 50 | 1 |  |  |  |
| CustomerCode | nvarchar | 100 | 0 |  |  |  |
| EntityUseCode | nvarchar | 50 | 1 |  |  |  |
| LineNum | nvarchar | 20 | 0 |  |  |  |
| TaxCode | nvarchar | 50 | 1 |  |  |  |
| TaxDate | smalldatetime | 4 | 1 |  |  |  |
| ItemCode | nvarchar | 100 | 1 |  |  |  |
| Description | nvarchar | 510 | 1 |  |  |  |
| Qty | numeric | 9 | 1 |  |  |  |
| Amount | money | 8 | 0 |  |  |  |
| Taxable | money | 8 | 1 |  |  |  |
| Discount | money | 8 | 1 |  |  |  |
| TotalTax | money | 8 | 1 |  |  |  |
| CountryTax | money | 8 | 1 |  |  |  |
| StateTax | money | 8 | 1 |  |  |  |
| CountyTax | money | 8 | 1 |  |  |  |
| CityTax | money | 8 | 1 |  |  |  |
| Other1Tax | money | 8 | 1 |  |  |  |
| Other2Tax | money | 8 | 1 |  |  |  |
| Ref1 | nvarchar | 100 | 1 |  |  |  |
| Ref2 | nvarchar | 100 | 1 |  |  |  |
| ExemptionNo | nvarchar | 50 | 1 |  |  |  |
| RevAcct | nvarchar | 100 | 1 |  |  |  |
| TaxType | nvarchar | 2 | 1 |  |  |  |
| DestAddress | nvarchar | 100 | 1 |  |  |  |
| DestCity | nvarchar | 100 | 1 |  |  |  |
| DestRegion | nvarchar | 4 | 0 |  |  |  |
| DestPostalCode | nvarchar | 20 | 0 |  |  |  |
| DestCountry | nvarchar | 4 | 1 |  |  |  |
| OrigAddress | nvarchar | 100 | 1 |  |  |  |
| OrigCity | nvarchar | 100 | 1 |  |  |  |
| OrigRegion | nvarchar | 4 | 0 |  |  |  |
| OrigPostalCode | nvarchar | 20 | 0 |  |  |  |
| OrigCountry | nvarchar | 4 | 1 |  |  |  |
| LocationCode | nvarchar | 100 | 1 |  |  |  |
| SalesPersonCode | nvarchar | 50 | 1 |  |  |  |
| PurchaseOrderNo | nvarchar | 100 | 1 |  |  |  |
| CurrencyCode | nvarchar | 6 | 1 |  |  |  |
| ExchangeRate | numeric | 9 | 1 |  |  |  |
| ExchangeRateEffDate | smalldatetime | 4 | 1 |  |  |  |
| PaymentDate | smalldatetime | 4 | 1 |  |  |  |
| TaxIncluded | tinyint | 1 | 1 |  |  |  |
| DestTaxRegion | nvarchar | 20 | 1 |  |  |  |
| OrigTaxRegion | nvarchar | 20 | 1 |  |  |  |
| max_serial_no | numeric | 9 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
