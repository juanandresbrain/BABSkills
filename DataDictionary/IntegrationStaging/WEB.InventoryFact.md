# WEB.InventoryFact

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 4 | 0 |  |  |  |
| GTIN | varchar | 20 | 0 |  |  |  |
| PreviousGTIN | varchar | 20 | 1 |  |  |  |
| StyleCode | varchar | 6 | 0 |  |  |  |
| SKUDescription | varchar | 120 | 1 |  |  |  |
| QTY | int | 4 | 0 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| SellingGeography | varchar | 2 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CheckDate | datetime | 8 | 0 |  |  |  |
| SendData | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeInventoryFactFromWM](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWM.md)
- [IntegrationStaging: WEB.spMergeInventoryFactFromWMbackup20191208](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWMbackup20191208.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes_backup20221102](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes_backup20221102.md)

