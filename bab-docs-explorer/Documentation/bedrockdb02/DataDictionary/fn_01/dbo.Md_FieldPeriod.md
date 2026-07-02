# dbo.Md_FieldPeriod

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| field_period_id | int | 4 | 0 | YES |  |  |
| sql_template_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| label_1 | varchar | 30 | 0 |  |  |  |
| label_2 | varchar | 30 | 0 |  |  |  |
| description_1 | varchar | 255 | 1 |  |  |  |
| description_2 | varchar | 255 | 1 |  |  |  |
| range | bit | 1 | 0 |  |  |  |
| time_unit | smallint | 2 | 0 |  |  |  |
| validate_proc | varchar | 30 | 1 |  |  |  |
| lblinput_1 | varchar | 30 | 1 |  |  |  |
| txtarg_1 | bit | 1 | 0 |  |  |  |
| lblinput_2 | varchar | 30 | 1 |  |  |  |
| txtarg_2 | bit | 1 | 0 |  |  |  |
| summed | bit | 1 | 0 |  |  |  |
| heading_label_1 | varchar | 30 | 1 |  |  |  |
| heading_label_2 | varchar | 30 | 1 |  |  |  |
| range_sql | text | 16 | 1 |  |  |  |
| period_id | int | 4 | 1 |  |  |  |
| where_sql_template_id | int | 4 | 1 |  |  |  |
| resource_id_1 | numeric | 9 | 1 |  |  |  |
| resource_id_2 | numeric | 9 | 1 |  |  |  |
| label_resource_name | nvarchar | 510 | 1 |  |  |  |
| lblinput1_resource_name | nvarchar | 510 | 1 |  |  |  |
| lblinput2_resource_name | nvarchar | 510 | 1 |  |  |  |
| heading_label_resource_name | nvarchar | 510 | 1 |  |  |  |
| lblinput1_2 | varchar | 30 | 1 |  |  |  |
| lblinput2_2 | varchar | 30 | 1 |  |  |  |
| resource_id_3 | numeric | 9 | 1 |  |  |  |
| desc_resource_name | nvarchar | 510 | 1 |  |  |  |

