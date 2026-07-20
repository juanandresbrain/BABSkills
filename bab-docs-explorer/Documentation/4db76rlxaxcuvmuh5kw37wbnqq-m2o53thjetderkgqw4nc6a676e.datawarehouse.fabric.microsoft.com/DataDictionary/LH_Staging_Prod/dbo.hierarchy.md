# dbo.hierarchy

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_id | int | 4 | 1 |  |  |  |
| hierarchy_label | varchar | 8000 | 1 |  |  |  |
| hierarchy_type | int | 4 | 1 |  |  |  |
| alternate_flag | bit | 1 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
