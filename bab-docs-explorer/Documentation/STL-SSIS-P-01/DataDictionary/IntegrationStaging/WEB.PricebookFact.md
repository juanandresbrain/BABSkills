# WEB.PricebookFact

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 6 | 1 |  |  |  |
| CurrentPrice | decimal | 9 | 1 |  |  |  |
| OriginalPrice | decimal | 9 | 1 |  |  |  |
| SalePrice | decimal | 9 | 1 |  |  |  |
| Catalog | varchar | 2 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CheckDate | datetime | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spGoogleAdsInventoryLoad](../../StoredProcedures/IntegrationStaging/WEB.spGoogleAdsInventoryLoad.md)
- [IntegrationStaging: WEB.spMergePricebookFact](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookFact.md)
- [IntegrationStaging: WEB.spMergePricebookFact_BAK20220705](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookFact_BAK20220705.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes_backup20221102](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes_backup20221102.md)
- [IntegrationStaging: WEB.spOutputPricebooks](../../StoredProcedures/IntegrationStaging/WEB.spOutputPricebooks.md)
- [IntegrationStaging: WEB.spOutputPricebooks_BAK20240806](../../StoredProcedures/IntegrationStaging/WEB.spOutputPricebooks_BAK20240806.md)
- [IntegrationStaging: WEB.spOutputPricebooks_FULL](../../StoredProcedures/IntegrationStaging/WEB.spOutputPricebooks_FULL.md)

