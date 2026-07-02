# dbo.sysmaintplan_log

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| task_detail_id | uniqueidentifier | 16 | 0 | YES |  |  |
| plan_id | uniqueidentifier | 16 | 1 |  |  |  |
| subplan_id | uniqueidentifier | 16 | 1 |  | YES |  |
| start_time | datetime | 8 | 1 |  |  |  |
| end_time | datetime | 8 | 1 |  |  |  |
| succeeded | bit | 1 | 1 |  |  |  |
| logged_remotely | bit | 1 | 0 |  |  |  |
| source_server_name | nvarchar | 256 | 1 |  |  |  |
| plan_name | nvarchar | 256 | 1 |  |  |  |
| subplan_name | nvarchar | 256 | 1 |  |  |  |

