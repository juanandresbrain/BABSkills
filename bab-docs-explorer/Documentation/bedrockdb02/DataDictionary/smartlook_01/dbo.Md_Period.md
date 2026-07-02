# dbo.Md_Period

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| period_id | int | 4 | 0 | YES |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| table_id | int | 4 | 0 |  |  |  |
| period_group_id | int | 4 | 0 |  |  |  |
| period_label_1 | varchar | 30 | 0 |  |  |  |
| period_label_2 | varchar | 30 | 0 |  |  |  |
| period_description_1 | varchar | 255 | 1 |  |  |  |
| period_description_2 | varchar | 255 | 1 |  |  |  |
| period_start_exp | varchar | 255 | 0 |  |  |  |
| all_dimensions | bit | 1 | 0 |  |  |  |
| have_sub_periods | tinyint | 1 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |

