# Reporting.AptosTo3plValidation

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DynamicsOrderId | varchar | 20 | 1 |  |  |  |
| AptosExportDocumentNumber | varchar | 20 | 1 |  |  |  |
| distribution_number | varchar | 20 | 1 |  |  |  |
| distribution_line_number | int | 4 | 1 |  |  |  |
| warehouse | varchar | 4 | 1 |  |  |  |
| location_code | varchar | 10 | 1 |  |  |  |
| rec_type | varchar | 10 | 1 |  |  |  |
| rec_label | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date_from_Aptos | datetime | 8 | 1 |  |  |  |
| ShipmentDocumentNumber3PL | bigint | 8 | 1 |  |  |  |
| ShipmentDocument3PLExportDate | datetime | 8 | 1 |  |  |  |

