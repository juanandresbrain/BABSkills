# dbo.reportingvatdiscoveryavalarap12

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DocumentType | float | 8 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| InvoiceDate | datetime2 | 8 | 1 |  |  |  |
| Currency | varchar | 8000 | 1 |  |  |  |
| VATCode | varchar | 8000 | 1 |  |  |  |
| SupplierID | float | 8 | 1 |  |  |  |
| SupplierName | varchar | 8000 | 1 |  |  |  |
| SupplierCountry | varchar | 8000 | 1 |  |  |  |
| SupplierVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| SupplierCountryVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| CustomerID | float | 8 | 1 |  |  |  |
| CustomerName | float | 8 | 1 |  |  |  |
| CustomerCountry | varchar | 8000 | 1 |  |  |  |
| CustomerVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| CustomerCountryVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| TaxableBasis | float | 8 | 1 |  |  |  |
| ValueVAT | float | 8 | 1 |  |  |  |
| TotalValueLine | float | 8 | 1 |  |  |  |
| AmountVATDeducted | float | 8 | 1 |  |  |  |
| AmountVATReverseCharged | float | 8 | 1 |  |  |  |
