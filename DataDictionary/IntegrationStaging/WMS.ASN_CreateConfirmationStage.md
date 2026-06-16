# WMS.ASN_CreateConfirmationStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| messageId | nvarchar | 510 | 1 |  |  |  |
| hasErrors | bit | 1 | 1 |  |  |  |
| Message | nvarchar | 510 | 1 |  |  |  |
| errorMessage | nvarchar | 8000 | 1 |  |  |  |
| _upstream.EnqueuedTimeUTC | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeASNCreateConfirmation](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateConfirmation.md)
- [IntegrationStaging: WMS.spMergeASNCreateConfirmation_BAK20260512](../../StoredProcedures/IntegrationStaging/WMS.spMergeASNCreateConfirmation_BAK20260512.md)

