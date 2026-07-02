# dbo.plan_mlid_xref

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_mlid_xref_id | decimal | 9 | 0 | YES |  |  |
| structure_id | int | 4 | 0 |  |  |  |
| tree_structure_id | int | 4 | 0 |  |  |  |
| planning_level_id | int | 4 | 0 |  |  |  |
| entity_type | smallint | 2 | 0 |  |  |  |
| entity_type_id | decimal | 9 | 0 |  |  |  |
| entity_id | decimal | 9 | 0 |  |  |  |
| entity_code | nvarchar | 46 | 0 |  |  |  |
| att_parent_type | tinyint | 1 | 0 |  |  |  |
| att_parent_id | decimal | 9 | 0 |  |  |  |
| merch_comp_id | int | 4 | 1 |  |  |  |
| div_code | nvarchar | 40 | 1 |  |  |  |
| level_seq_no | smallint | 2 | 0 |  |  |  |
| guest_level | smallint | 2 | 0 |  |  |  |
| owner_structure | nvarchar | 100 | 0 |  |  |  |
| owner_mlid_path | nvarchar | 100 | 1 |  |  |  |
| owner_mlid_alias | nvarchar | 44 | 1 |  |  |  |
| owner_mlid_alias_div | nvarchar | 44 | 1 |  |  |  |
| mlid | nvarchar | 60 | 0 |  |  |  |
| description | nvarchar | 100 | 0 |  |  |  |
| abbreviation | nvarchar | 20 | 0 |  |  |  |
| alias | nvarchar | 44 | 0 |  |  |  |
| alias_div | nvarchar | 44 | 0 |  |  |  |
| guest_of_structure | nvarchar | 100 | 1 |  |  |  |
| guest_of_owner_mlid_path | nvarchar | 100 | 1 |  |  |  |
| guest_of_owner_mlid_alias | nvarchar | 44 | 1 |  |  |  |
| core_replication_queue_id | decimal | 9 | 1 |  |  |  |

