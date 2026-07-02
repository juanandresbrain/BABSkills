# WMS.ValidationAptosDistroAfterSplit

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | varchar | 50 | 1 |  |  |  |
| distribution_line_number | int | 4 | 1 |  |  |  |
| SourceID | varchar | 20 | 1 |  |  |  |
| DestID | varchar | 21 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| release_date | datetime | 8 | 1 |  |  |  |
| StoreShipmentNumber | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailAptosDistributionExportValidation](../../StoredProcedures/IntegrationStaging/WMS.spEmailAptosDistributionExportValidation.md)

