# WMS.DynamicsTo3PLOrderExportTimCBackup20220811Support

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RecID | int | 4 | 0 |  |  |  |
| sourceid | varchar | 4 | 0 |  |  |  |
| destid | varchar | 5 | 0 |  |  |  |
| rec_type | varchar | 6 | 0 |  |  |  |
| message | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | varchar | 30 | 1 |  |  |  |
| distribution_number | varchar | 50 | 0 |  |  |  |
| ref_field_1 | int | 4 | 0 |  |  |  |
| DynamicsOrderId | varchar | 20 | 1 |  |  |  |
| short_desc | varchar | 52 | 1 |  |  |  |
| vendor_style | varchar | 6 | 1 |  |  |  |
| color_code | varchar | 2 | 1 |  |  |  |
| document_number | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| ExportDate | datetime | 8 | 1 |  |  |  |
| SummaryReportExported | datetime | 8 | 1 |  |  |  |

