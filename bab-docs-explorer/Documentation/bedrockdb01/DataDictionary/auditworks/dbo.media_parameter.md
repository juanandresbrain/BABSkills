# dbo.media_parameter

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_no | smallint | 2 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| acceptable_short_limit | money | 8 | 0 |  |  |  |
| deposit_category | smallint | 2 | 0 |  |  |  |
| deposit_source | smallint | 2 | 0 |  |  |  |
| deposit_destination | smallint | 2 | 0 |  |  |  |
| media_not_counted | tinyint | 1 | 0 |  |  |  |
| variance_is_short | tinyint | 1 | 0 |  |  |  |
| variance_is_lost_doc | tinyint | 1 | 0 |  |  |  |
| verify_card_type_edit | tinyint | 1 | 0 |  |  |  |
| verify_card_type_manual | tinyint | 1 | 0 |  |  |  |
