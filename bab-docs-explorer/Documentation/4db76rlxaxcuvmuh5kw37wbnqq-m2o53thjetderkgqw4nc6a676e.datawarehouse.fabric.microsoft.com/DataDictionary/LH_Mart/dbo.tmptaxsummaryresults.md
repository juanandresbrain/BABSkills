# dbo.tmptaxsummaryresults

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DocumentType | varchar | 8000 | 1 |  |  |  |
| TransactionDate | varchar | 8000 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| InvoiceDate | varchar | 8000 | 1 |  |  |  |
| Currency | varchar | 8000 | 1 |  |  |  |
| VATCode | varchar | 8000 | 1 |  |  |  |
| SupplierID | varchar | 8000 | 1 |  |  |  |
| SupplierName | varchar | 8000 | 1 |  |  |  |
| SupplierCountry | varchar | 8000 | 1 |  |  |  |
| SupplierVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| SupplierCountryVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| CustomerID | varchar | 8000 | 1 |  |  |  |
| CustomerName | varchar | 8000 | 1 |  |  |  |
| CustomerCountry | varchar | 8000 | 1 |  |  |  |
| CustomerVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| CustomerCountryVATNumberUsed | varchar | 8000 | 1 |  |  |  |
| TaxableBasis | decimal | 9 | 1 |  |  |  |
| ValueVAT | decimal | 9 | 1 |  |  |  |
| TotalValueLine | decimal | 9 | 1 |  |  |  |
| AmountVATDeducted | decimal | 9 | 1 |  |  |  |
| AmountVATReverseCharged | decimal | 9 | 1 |  |  |  |
