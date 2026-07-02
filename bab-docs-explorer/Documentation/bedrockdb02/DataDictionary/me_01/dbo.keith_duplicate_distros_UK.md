# dbo.keith_duplicate_distros_UK

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_number | varchar | 20 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| color_code | varchar | 3 | 0 |  |  |  |
| dist_line_id | int | 4 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| release_date | smalldatetime | 4 | 1 |  |  |  |
| location_code | varchar | 20 | 0 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |

