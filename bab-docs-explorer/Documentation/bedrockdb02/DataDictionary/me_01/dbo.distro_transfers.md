# dbo.distro_transfers

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| sourceid | int | 4 | 0 |  |  |  |
| destid | int | 4 | 0 |  |  |  |
| upc_number | int | 4 | 0 |  |  |  |
| quantity | int | 4 | 0 |  |  |  |
| groupinglabel | varchar | 20 | 1 |  |  |  |
| description | varchar | 20 | 1 |  |  |  |
| rec_type | int | 4 | 0 |  |  |  |
| loaded_date | datetime | 8 | 0 |  |  |  |
| documentnumber | varchar | 9 | 1 |  |  |  |
| linenumber | int | 4 | 1 |  |  |  |
| reasoncode | varchar | 5 | 1 |  |  |  |
| exported_date | datetime | 8 | 1 |  |  |  |
| tpm_exported_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spDistroTransfers_Archive](../../StoredProcedures/me_01/dbo.spDistroTransfers_Archive.md)
- [me_01: dbo.spMerchandisingDistroImport](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport.md)
- [me_01: dbo.spMerchandisingDistroImport_BAK_20181119](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImport_BAK_20181119.md)
- [me_01: dbo.spMerchandisingDistroImportBACKUP20150909](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportBACKUP20150909.md)
- [me_01: dbo.spMerchandisingDistroTransfersValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroTransfersValidation.md)
- [me_01: dbo.spMerchandisingEmailCostcoDistroValidation](../../StoredProcedures/me_01/dbo.spMerchandisingEmailCostcoDistroValidation.md)
- [me_01: dbo.spMerchandisingImportDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingImportDistributions.md)
- [me_01: dbo.spMerchandisingSelectCostcoDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCostcoDistributions.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)

