# dbo.tmpcapotransfers

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_number | varchar | 8000 | 1 |  |  |  |
| carton_label | varchar | 8000 | 1 |  |  |  |
| from_location_code | varchar | 4 | 0 |  |  |  |
| to_location_code | varchar | 4 | 0 |  |  |  |
| date_shipped | char | 30 | 1 |  |  |  |
| reason_code | varchar | 4 | 0 |  |  |  |
| Grouping_Label | varchar | 17 | 0 |  |  |  |
| upc | varchar | 26 | 0 |  |  |  |
| send_units | int | 4 | 1 |  |  |  |

