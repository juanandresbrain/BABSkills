# WEB.PricebookBundleSkuFact

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BundleSku | varchar | 150 | 1 |  |  |  |
| BundleDisplayName | varchar | 150 | 1 |  |  |  |
| BundleSkuPrice | decimal | 9 | 1 |  |  |  |
| BundleSkuCatalog | varchar | 2 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CheckDate | datetime | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergePricebookBundleSkuFact](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookBundleSkuFact.md)
- [IntegrationStaging: WEB.spMergePricebookBundleSkuFact_Bak20241003](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookBundleSkuFact_Bak20241003.md)
- [IntegrationStaging: WEB.spOutputPricebooks](../../StoredProcedures/IntegrationStaging/WEB.spOutputPricebooks.md)

