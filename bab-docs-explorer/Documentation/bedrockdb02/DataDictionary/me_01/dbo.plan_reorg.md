# dbo.plan_reorg

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_reorg_id | decimal | 9 | 0 | YES |  |  |
| owner_structure | nvarchar | 100 | 0 |  |  |  |
| owner_mlid_path | nvarchar | 100 | 1 |  |  |  |
| owner_mlid_alias | nvarchar | 44 | 1 |  |  |  |
| mlid | nvarchar | 60 | 0 |  |  |  |
| alias | nvarchar | 44 | 0 |  |  |  |
| new_owner_structure | nvarchar | 100 | 1 |  |  |  |
| new_owner_mlid_path | nvarchar | 100 | 1 |  |  |  |
| new_owner_mlid_alias | nvarchar | 44 | 1 |  |  |  |
| new_alias | nvarchar | 44 | 1 |  |  |  |
| transaction_code | nvarchar | 2 | 0 |  |  |  |
| core_replication_queue_id | decimal | 9 | 1 |  |  |  |

