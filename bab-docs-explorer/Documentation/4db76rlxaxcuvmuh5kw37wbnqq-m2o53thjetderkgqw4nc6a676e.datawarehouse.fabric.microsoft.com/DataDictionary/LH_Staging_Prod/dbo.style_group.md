# dbo.style_group

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
