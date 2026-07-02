# dbo.rounding_rule

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rounding_rule_id | decimal | 9 | 0 | YES |  |  |
| rounding_rule_code | nvarchar | 40 | 0 |  |  |  |
| rounding_rule_description | nvarchar | 120 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| rounding_rule_type | smallint | 2 | 0 |  |  |  |
| ending_rule | smallint | 2 | 0 |  |  |  |
| value1 | decimal | 9 | 1 |  |  |  |
| value2 | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

