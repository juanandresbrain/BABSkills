# dbo.ReportingVatDiscoveryAvalaraP12

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DocumentType | float | 8 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| InvoiceNumber | nvarchar | 510 | 1 |  |  |  |
| InvoiceDate | datetime | 8 | 1 |  |  |  |
| Currency | nvarchar | 510 | 1 |  |  |  |
| VATCode | nvarchar | 510 | 1 |  |  |  |
| SupplierID | float | 8 | 1 |  |  |  |
| SupplierName | nvarchar | 510 | 1 |  |  |  |
| SupplierCountry | nvarchar | 510 | 1 |  |  |  |
| SupplierVATNumberUsed | nvarchar | 510 | 1 |  |  |  |
| SupplierCountryVATNumberUsed | nvarchar | 510 | 1 |  |  |  |
| CustomerID | float | 8 | 1 |  |  |  |
| CustomerName | float | 8 | 1 |  |  |  |
| CustomerCountry | nvarchar | 510 | 1 |  |  |  |
| CustomerVATNumberUsed | nvarchar | 510 | 1 |  |  |  |
| CustomerCountryVATNumberUsed | nvarchar | 510 | 1 |  |  |  |
| TaxableBasis | float | 8 | 1 |  |  |  |
| ValueVAT | float | 8 | 1 |  |  |  |
| TotalValueLine | float | 8 | 1 |  |  |  |
| AmountVATDeducted | float | 8 | 1 |  |  |  |
| AmountVATReverseCharged | float | 8 | 1 |  |  |  |
