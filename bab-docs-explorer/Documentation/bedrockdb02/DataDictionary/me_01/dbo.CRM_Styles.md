# dbo.CRM_Styles

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | int | 4 | 0 |  |  |  |
| vendor_code | char | 6 | 0 |  |  |  |
| class_code | int | 4 | 0 |  |  |  |
| subclass_code | smallint | 2 | 0 |  |  |  |
| vendor_style | varchar | 20 | 1 |  |  |  |
| style_aka | varchar | 20 | 0 |  |  |  |
| style_description | varchar | 30 | 0 |  |  |  |
| merchandising_active_flag | bit | 1 | 0 |  |  |  |
| retail | money | 8 | 0 |  |  |  |
| cost | money | 8 | 0 |  |  |  |
| style_grouping_code_a | varchar | 8 | 1 |  |  |  |
| style_grouping_code_b | varchar | 8 | 1 |  |  |  |
| style_grouping_code_c | varchar | 8 | 1 |  |  |  |
| style_grouping_code_d | varchar | 8 | 1 |  |  |  |
| style_grouping_code_e | varchar | 8 | 1 |  |  |  |
| style_grouping_code_f | varchar | 8 | 1 |  |  |  |
| timestamp | varbinary | 8 | 1 |  |  |  |

