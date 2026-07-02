# WMS.DynamicsTo3PLOrderExport

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RecID | int | 4 | 0 |  |  |  |
| sourceid | varchar | 4 | 0 | YES |  |  |
| destid | varchar | 10 | 0 | YES |  |  |
| rec_type | varchar | 6 | 0 | YES |  |  |
| message | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 0 | YES |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 50 | 0 | YES |  |  |
| ref_field_1 | int | 4 | 0 | YES |  |  |
| DynamicsOrderId | varchar | 20 | 1 |  |  |  |
| short_desc | varchar | 52 | 1 |  |  |  |
| vendor_style | varchar | 6 | 1 |  |  |  |
| color_code | varchar | 2 | 1 |  |  |  |
| document_number | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |
| SummaryReportExported | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMerchandisingReportStoreShipmentExportConfirmationUK](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingReportStoreShipmentExportConfirmationUK.md)
- [IntegrationStaging: WMS.spMerchandisingReportStoreShipmentExportConfirmationWC](../../StoredProcedures/IntegrationStaging/WMS.spMerchandisingReportStoreShipmentExportConfirmationWC.md)
- [IntegrationStaging: WMS.spMergeDynamicsTo3PLOrderExport](../../StoredProcedures/IntegrationStaging/WMS.spMergeDynamicsTo3PLOrderExport.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesCN](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesCN.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesCN_BAK20220804](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesCN_BAK20220804.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesCN_BAK20220825](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesCN_BAK20220825.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesUK](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesUK.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesUK_BAK20220825](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesUK_BAK20220825.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesWC](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesWC.md)
- [IntegrationStaging: WMS.spOutputDynamicsDistroFilesWC_BAK20220825](../../StoredProcedures/IntegrationStaging/WMS.spOutputDynamicsDistroFilesWC_BAK20220825.md)

