# dbo.min_max_wos_param

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| min_max_wos_param_id | bigint | 8 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| review_on_sunday | bit | 1 | 0 |  |  |  |
| review_on_monday | bit | 1 | 0 |  |  |  |
| review_on_tuesday | bit | 1 | 0 |  |  |  |
| review_on_wednesday | bit | 1 | 0 |  |  |  |
| review_on_thursday | bit | 1 | 0 |  |  |  |
| review_on_friday | bit | 1 | 0 |  |  |  |
| review_on_saturday | bit | 1 | 0 |  |  |  |
| cycle_frequency | smallint | 2 | 0 |  |  |  |
| last_execution | smalldatetime | 4 | 1 |  |  |  |
| last_number_of_weeks | smallint | 2 | 1 |  |  |  |
| minimum_weeks_of_supply | smallint | 2 | 1 |  |  |  |
| maximum_weeks_of_supply | smallint | 2 | 1 |  |  |  |
| process_level | tinyint | 1 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| cycle_period | tinyint | 1 | 0 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| next_execution | smalldatetime | 4 | 1 |  |  |  |
| use_seasonality | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingInsertMinMaxProfileArchive](../../StoredProcedures/me_01/dbo.spMerchandisingInsertMinMaxProfileArchive.md)

