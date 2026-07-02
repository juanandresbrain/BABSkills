# WMS.ASN_CreateConfirmation

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AsnShipmentNumber | nvarchar | 30 | 1 |  |  |  |
| messageId | nvarchar | 510 | 1 |  |  |  |
| hasErrors | bit | 1 | 1 |  |  |  |
| Message | nvarchar | 510 | 1 |  |  |  |
| errorMessage | nvarchar | 8000 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |
| EnqueuedTimeCST | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeASNCreateConfirmation](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateConfirmation.md)
- [IntegrationStaging: WMS.spMergeASNCreateConfirmation_BAK20260512](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateConfirmation_BAK20260512.md)
- [IntegrationStaging: WMS.spMergeASNCreateEmails](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateEmails.md)
- [IntegrationStaging: WMS.spMergeASNCreateEmails_BAK20260513](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateEmails_BAK20260513.md)
- [IntegrationStaging: WMS.spReportTPMtoD365errors](../../StoredProcedures/IntegrationStaging/WMS.spReportTPMtoD365errors.md)

