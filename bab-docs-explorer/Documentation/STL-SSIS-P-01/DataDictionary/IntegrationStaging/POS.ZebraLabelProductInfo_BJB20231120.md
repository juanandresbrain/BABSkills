# POS.ZebraLabelProductInfo_BJB20231120

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| cost | varchar | 14 | 1 |  |  |  |
| local_desc | nvarchar | 80 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 0 |  |  |  |
| in_date | datetime | 8 | 1 |  |  |  |

