# WMS.DBSchenkerFullInGateFileStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrder | varchar | 50 | 1 |  |  |  |
| ProductCode | varchar | 50 | 1 |  |  |  |
| ShippedQty | varchar | 50 | 1 |  |  |  |
| FullIngateatLoadPort | varchar | 52 | 1 |  |  |  |
| POL | varchar | 50 | 1 |  |  |  |
| MANUFACTURERCODE | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDBSchenkerFullInGateFile](../../StoredProcedures/IntegrationStaging/WMS.spMergeDBSchenkerFullInGateFile.md)

