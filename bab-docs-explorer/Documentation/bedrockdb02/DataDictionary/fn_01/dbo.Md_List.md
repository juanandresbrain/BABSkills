# dbo.Md_List

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| list_id | int | 4 | 0 | YES |  |  |
| list_label_1 | varchar | 30 | 0 |  |  |  |
| list_label_2 | varchar | 30 | 0 |  |  |  |
| list_description_1 | varchar | 255 | 1 |  |  |  |
| list_description_2 | varchar | 255 | 1 |  |  |  |
| order_method | tinyint | 1 | 0 |  |  |  |
| display_method | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |

