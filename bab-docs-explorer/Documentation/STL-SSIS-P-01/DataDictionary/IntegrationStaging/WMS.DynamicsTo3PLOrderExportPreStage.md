# WMS.DynamicsTo3PLOrderExportPreStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sourceid | varchar | 4 | 1 |  |  |  |
| destid | varchar | 10 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| message | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 50 | 1 |  |  |  |
| ref_field_1 | int | 4 | 1 |  |  |  |
| short_desc | varchar | 75 | 1 |  |  |  |
| vendor_style | varchar | 6 | 1 |  |  |  |
| color_code | varchar | 2 | 1 |  |  |  |
| document_number | bigint | 8 | 1 |  |  |  |
| DynamicsOrderId | varchar | 20 | 1 |  |  |  |

