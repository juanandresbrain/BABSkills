# dbo.babw_mtdVijl2

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DocumentType | int | 4 | 1 |  |  |  |
| TransactionDate | nvarchar | 100 | 1 |  |  |  |
| InvoiceNumber | nvarchar | 100 | 1 |  |  |  |
| InvoiceDate | nvarchar | 100 | 1 |  |  |  |
| Currency | nvarchar | 100 | 1 |  |  |  |
| VATCode | nvarchar | 100 | 1 |  |  |  |
| SupplierID | nvarchar | 100 | 1 |  |  |  |
| SupplierName | nvarchar | 200 | 1 |  |  |  |
| SupplierCountry | nvarchar | 100 | 1 |  |  |  |
| SupplierVATNumberUsed | nvarchar | 100 | 1 |  |  |  |
| SupplierCountryVATNumberUsed | nvarchar | 100 | 1 |  |  |  |
| CustomerID | nvarchar | 100 | 1 |  |  |  |
| CustomerName | nvarchar | 100 | 1 |  |  |  |
| CustomerCountry | nvarchar | 100 | 1 |  |  |  |
| CustomerVATNumberUsed | nvarchar | 100 | 1 |  |  |  |
| CustomerCountryVATNumberUsed | nvarchar | 100 | 1 |  |  |  |
| TaxableBasis | decimal | 9 | 1 |  |  |  |
| ValueVAT | decimal | 9 | 1 |  |  |  |
| TotalValueLine | decimal | 9 | 1 |  |  |  |
| AmountVATDeducted | decimal | 9 | 1 |  |  |  |
| AmountVATReverseCharged | decimal | 9 | 1 |  |  |  |
| SupplierInvoiceNumber | nvarchar | 100 | 1 |  |  |  |
| sequenceNumber | int | 4 | 1 |  |  |  |
| TAXTRANS_RECID | nvarchar | 510 | 1 |  |  |  |

