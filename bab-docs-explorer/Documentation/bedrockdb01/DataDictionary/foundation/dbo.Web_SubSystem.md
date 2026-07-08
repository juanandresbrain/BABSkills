# dbo.Web_SubSystem

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 1 |  |  |  |
| label | varchar | 255 | 0 |  |  |  |
| display_label | varchar | 255 | 1 |  |  |  |
| default_start_page | varchar | 255 | 1 |  |  |  |
| legacy_topic_id | int | 4 | 1 |  |  |  |
| root_path | varchar | 255 | 1 |  |  |  |
