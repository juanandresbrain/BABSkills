# dbo.Web_NavDescription

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| parent_id | int | 4 | 0 |  |  |  |
| display_id | int | 4 | 0 |  |  |  |
| subsystem_id | int | 4 | 0 |  |  |  |
| label | varchar | 255 | 0 |  |  |  |
| url | varchar | 255 | 1 |  |  |  |
| description | varchar | 255 | 1 |  |  |  |
| menu_type | int | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| security_token | varchar | 11 | 1 |  |  |  |
| indent_level | int | 4 | 1 |  |  |  |

