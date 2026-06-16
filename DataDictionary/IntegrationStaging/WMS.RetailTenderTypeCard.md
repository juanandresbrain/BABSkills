# WMS.RetailTenderTypeCard

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CardIssuer | nvarchar | 8000 | 1 |  |  |  |
| CardProcessorCode | nvarchar | 8000 | 1 |  |  |  |
| CardTypeId | nvarchar | 8000 | 1 |  |  |  |
| CardTypes | nvarchar | 510 | 1 |  |  |  |
| Name | nvarchar | 8000 | 1 |  |  |  |
| PaymentSystem | nvarchar | 510 | 1 |  |  |  |
| RetailChannel | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeRetailTenderTypeCard](../../StoredProcedures/IntegrationStaging/WMS.spMergeRetailTenderTypeCard.md)

