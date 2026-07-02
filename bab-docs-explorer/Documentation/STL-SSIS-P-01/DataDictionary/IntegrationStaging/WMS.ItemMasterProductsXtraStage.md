# WMS.ItemMasterProductsXtraStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AreIdenticalConfigurationsAllowed | nvarchar | 510 | 1 |  |  |  |
| HarmonizedSystemCode | nvarchar | 8000 | 1 |  |  |  |
| IsAutomaticVariantGenerationEnabled | nvarchar | 510 | 1 |  |  |  |
| IsCatchWeightProduct | nvarchar | 510 | 1 |  |  |  |
| IsProductKit | nvarchar | 510 | 1 |  |  |  |
| IsProductVariantUnitConversionEnabled | nvarchar | 510 | 1 |  |  |  |
| NMFCCode | nvarchar | 8000 | 1 |  |  |  |
| PlannedOrders | nvarchar | -1 | 1 |  |  |  |
| ProductAttributeValues | nvarchar | -1 | 1 |  |  |  |
| ProductCategoryAssignments | nvarchar | -1 | 1 |  |  |  |
| ProductColorGroupId | nvarchar | 8000 | 1 |  |  |  |
| ProductDescription | nvarchar | 8000 | 1 |  |  |  |
| ProductDimensionGroupName | nvarchar | 8000 | 1 |  |  |  |
| ProductDocumentAttachments | nvarchar | -1 | 1 |  |  |  |
| ProductName | nvarchar | 8000 | 1 |  |  |  |
| ProductNumber | nvarchar | 8000 | 1 |  |  |  |
| ProductSearchName | nvarchar | 8000 | 1 |  |  |  |
| ProductSizeGroupId | nvarchar | 8000 | 1 |  |  |  |
| ProductStyleGroupId | nvarchar | 8000 | 1 |  |  |  |
| ProductSubType | nvarchar | 510 | 1 |  |  |  |
| ProductType | nvarchar | 510 | 1 |  |  |  |
| ProductVariantNameNomenclatureName | nvarchar | 8000 | 1 |  |  |  |
| ProductVariantNumberNomenclatureName | nvarchar | 8000 | 1 |  |  |  |
| ReleasedProducts | nvarchar | -1 | 1 |  |  |  |
| RetailProductCategoryName | nvarchar | 8000 | 1 |  |  |  |
| STCCCode | nvarchar | 8000 | 1 |  |  |  |
| StorageDimensionGroupName | nvarchar | 8000 | 1 |  |  |  |
| TrackingDimensionGroupName | nvarchar | 8000 | 1 |  |  |  |
| VariantConfigurationTechnology | nvarchar | 510 | 1 |  |  |  |
| Entity | nvarchar | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeItemMasterProductsXtra](../../StoredProcedures/IntegrationStaging/WMS.spMergeItemMasterProductsXtra.md)

