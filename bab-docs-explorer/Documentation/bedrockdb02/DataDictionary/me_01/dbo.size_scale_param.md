# dbo.size_scale_param

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| size_scale_param_id | bigint | 8 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| review_on_sunday | bit | 1 | 0 |  |  |  |
| review_on_monday | bit | 1 | 0 |  |  |  |
| review_on_tuesday | bit | 1 | 0 |  |  |  |
| review_on_wednesday | bit | 1 | 0 |  |  |  |
| review_on_thursday | bit | 1 | 0 |  |  |  |
| review_on_friday | bit | 1 | 0 |  |  |  |
| review_on_saturday | bit | 1 | 0 |  |  |  |
| cycle_frequency | smallint | 2 | 0 |  |  |  |
| last_execution | smalldatetime | 4 | 1 |  |  |  |
| merch_year_week_from | int | 4 | 1 |  |  |  |
| merch_year_week_to | int | 4 | 1 |  |  |  |
| last_number_of_weeks | tinyint | 1 | 1 |  |  |  |
| at_merch_group_level_flag | bit | 1 | 0 |  |  |  |
| at_style_size_level_flag | bit | 1 | 0 |  |  |  |
| at_style_color_size_level_flag | bit | 1 | 0 |  |  |  |
| chain_level_flag | bit | 1 | 0 |  |  |  |
| last_modified_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| cycle_period | tinyint | 1 | 0 |  |  |  |
| application_server_id | T_ID | 16 | 0 |  |  |  |
| next_execution | smalldatetime | 4 | 1 |  |  |  |
| sales_hist_price_point | tinyint | 1 | 0 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| generate_job_type | tinyint | 1 | 0 |  |  |  |

