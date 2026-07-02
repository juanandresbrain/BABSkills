# dbo.systargetservergroups

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| servergroup_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_targetservergroup](../../StoredProcedures/msdb/dbo.sp_add_targetservergroup.md)
- [msdb: dbo.sp_add_targetsvrgrp_member](../../StoredProcedures/msdb/dbo.sp_add_targetsvrgrp_member.md)
- [msdb: dbo.sp_apply_job_to_targets](../../StoredProcedures/msdb/dbo.sp_apply_job_to_targets.md)
- [msdb: dbo.sp_delete_targetservergroup](../../StoredProcedures/msdb/dbo.sp_delete_targetservergroup.md)
- [msdb: dbo.sp_delete_targetsvrgrp_member](../../StoredProcedures/msdb/dbo.sp_delete_targetsvrgrp_member.md)
- [msdb: dbo.sp_help_targetservergroup](../../StoredProcedures/msdb/dbo.sp_help_targetservergroup.md)
- [msdb: dbo.sp_update_targetservergroup](../../StoredProcedures/msdb/dbo.sp_update_targetservergroup.md)

