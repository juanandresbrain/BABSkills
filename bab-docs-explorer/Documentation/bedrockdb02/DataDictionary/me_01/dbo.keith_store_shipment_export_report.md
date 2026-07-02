# dbo.keith_store_shipment_export_report

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_number | decimal | 9 | 1 |  |  |  |
| location_code | varchar | 4 | 1 |  |  |  |
| rec_label | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 6 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| exported | int | 4 | 0 |  |  |  |

