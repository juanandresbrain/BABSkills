# dbo.charge

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| charge_id | smallint | 2 | 0 | YES |  |  |
| charge_code | nvarchar | 16 | 0 |  |  |  |
| charge_description | nvarchar | 60 | 0 |  |  |  |
| charge_value | decimal | 9 | 0 |  |  |  |
| use_percent_for_charge_flag | bit | 1 | 0 |  |  |  |
| currency_id | decimal | 9 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

