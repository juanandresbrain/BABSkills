# WMS.ValidateAptosPOtoStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PONumber | varchar | 20 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| VendorCode | varchar | 10 | 1 |  |  |  |
| FactoryCode | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailPOExportSummary](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummary.md)
- [IntegrationStaging: WMS.spEmailPOExportSummaryBAK20220801](../../StoredProcedures/IntegrationStaging/WMS.spEmailPOExportSummaryBAK20220801.md)

