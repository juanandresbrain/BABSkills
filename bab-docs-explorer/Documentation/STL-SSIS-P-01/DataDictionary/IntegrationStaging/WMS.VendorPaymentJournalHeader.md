# WMS.VendorPaymentJournalHeader

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CategoryPurpose | bigint | 8 | 1 |  |  |  |
| ChargeBearer | bigint | 8 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| Description | nvarchar | 8000 | 1 |  |  |  |
| IsPosted | nvarchar | 510 | 1 |  |  |  |
| JournalBatchNumber | nvarchar | 8000 | 1 |  |  |  |
| JournalName | nvarchar | 8000 | 1 |  |  |  |
| LocalInstrument | bigint | 8 | 1 |  |  |  |
| OverrideSalesTax | nvarchar | 510 | 1 |  |  |  |
| ServiceLevel | bigint | 8 | 1 |  |  |  |
| VendorPaymentJournalHeaderEntityRole | nvarchar | -1 | 1 |  |  |  |
| VendorPaymentJournalLine | nvarchar | -1 | 1 |  |  |  |

