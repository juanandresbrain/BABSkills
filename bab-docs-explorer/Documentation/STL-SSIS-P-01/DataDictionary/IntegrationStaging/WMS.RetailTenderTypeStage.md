# WMS.RetailTenderTypeStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DefaultFunction | nvarchar | 510 | 1 |  |  |  |
| Name | nvarchar | 8000 | 1 |  |  |  |
| PaymentMethodNumber | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeRetailTenderType](../../StoredProcedures/IntegrationStaging/WMS.spMergeRetailTenderType.md)

