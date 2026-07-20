# dbo.style_group_sqlsynccopy

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_group_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| main_group_flag | bit | 1 | 1 |  |  |  |
| reclass_pending_flag | bit | 1 | 1 |  |  |  |
| reclass_to_group_id | int | 4 | 1 |  |  |  |
| reclass_move_history_flag | bit | 1 | 1 |  |  |  |
