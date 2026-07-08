# dbo.tmpVatSummaryResults

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DocumentType | varchar | 50 | 1 |  |  |  |
| TransactionDate | varchar | 50 | 1 |  |  |  |
| InvoiceNumber | varchar | 50 | 1 |  |  |  |
| InvoiceDate | varchar | 50 | 1 |  |  |  |
| Currency | varchar | 50 | 1 |  |  |  |
| VATCode | varchar | 50 | 1 |  |  |  |
| SupplierID | varchar | 50 | 1 |  |  |  |
| SupplierName | varchar | 50 | 1 |  |  |  |
| SupplierCountry | varchar | 50 | 1 |  |  |  |
| SupplierVATNumberUsed | varchar | 50 | 1 |  |  |  |
| SupplierCountryVATNumberUsed | varchar | 50 | 1 |  |  |  |
| CustomerID | varchar | 50 | 1 |  |  |  |
| CustomerName | varchar | 50 | 1 |  |  |  |
| CustomerCountry | varchar | 50 | 1 |  |  |  |
| CustomerVATNumberUsed | varchar | 50 | 1 |  |  |  |
| CustomerCountryVATNumberUsed | varchar | 50 | 1 |  |  |  |
| TaxableBasis | numeric | 9 | 1 |  |  |  |
| ValueVAT | numeric | 9 | 1 |  |  |  |
| TotalValueLine | numeric | 9 | 1 |  |  |  |
| AmountVATDeducted | numeric | 9 | 1 |  |  |  |
| AmountVATReverseCharged | numeric | 9 | 1 |  |  |  |
