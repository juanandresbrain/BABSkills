# dbo.tmpWebSaleDetails

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 0 |  |  |  |
| LocationName | varchar | 6 | 0 |  |  |  |
| RetailTransactionID | int | 4 | 0 |  |  |  |
| StoreNumber | int | 4 | 0 |  |  |  |
| RetailTransactionNumber | int | 4 | 0 |  |  |  |
| TransactionID | int | 4 | 0 |  |  |  |
| WMOrderNumber | varchar | 53 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| InvoiceDate | datetime | 8 | 1 |  |  |  |
| InvoiceNumber | varchar | 50 | 1 |  |  |  |
| PaymentTransactionType | varchar | 50 | 1 |  |  |  |
| InvoiceAmount | money | 8 | 1 |  |  |  |
| SubTotal | money | 8 | 1 |  |  |  |
| Shipping | money | 8 | 1 |  |  |  |
| ProcessingFee | money | 8 | 1 |  |  |  |
| Tax | decimal | 17 | 1 |  |  |  |
| TransactionAmount | money | 8 | 1 |  |  |  |
| OrderDiscount | money | 8 | 1 |  |  |  |
| ItemDiscount | money | 8 | 1 |  |  |  |
| TotalCharges | money | 8 | 1 |  |  |  |

