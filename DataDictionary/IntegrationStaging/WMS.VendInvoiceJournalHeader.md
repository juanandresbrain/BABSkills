# WMS.VendInvoiceJournalHeader

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| Description | nvarchar | 8000 | 1 |  |  |  |
| IsPosted | nvarchar | 510 | 1 |  |  |  |
| JournalBatchNumber | nvarchar | 8000 | 1 |  |  |  |
| JournalName | nvarchar | 8000 | 1 |  |  |  |
| JournalTotalCredit | float | 8 | 1 |  |  |  |
| JournalTotalDebit | float | 8 | 1 |  |  |  |
| OverrideSalesTax | nvarchar | 510 | 1 |  |  |  |
| SalesTaxIncluded | nvarchar | 510 | 1 |  |  |  |
| VendInvoiceJournalLine | nvarchar | -1 | 1 |  |  |  |

