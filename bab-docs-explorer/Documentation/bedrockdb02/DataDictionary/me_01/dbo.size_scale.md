# dbo.size_scale

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| size_scale_id | decimal | 9 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| size_category_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| merch_level | tinyint | 1 | 0 |  |  |  |
| size_scale_type | tinyint | 1 | 0 |  |  |  |
| scale_type | tinyint | 1 | 0 |  |  |  |
| allow_system_override_flag | bit | 1 | 0 |  |  |  |
| size_scale_total | smallint | 2 | 0 |  |  |  |
| source | tinyint | 1 | 0 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| owner_application | tinyint | 1 | 0 |  |  |  |

