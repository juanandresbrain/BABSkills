# ERP.WCPalletReceipts

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReceiptDate | datetime | 8 | 1 |  |  |  |
| PalletID | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spPOReceiptsImportWC](../../StoredProcedures/IntegrationStaging/ERP.spPOReceiptsImportWC.md)

