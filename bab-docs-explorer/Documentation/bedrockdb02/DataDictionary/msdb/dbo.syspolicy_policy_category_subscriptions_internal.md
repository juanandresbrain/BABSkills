# dbo.syspolicy_policy_category_subscriptions_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| policy_category_subscription_id | int | 4 | 0 | YES |  |  |
| target_type | sysname | 256 | 0 |  |  |  |
| target_object | sysname | 256 | 0 |  |  |  |
| policy_category_id | int | 4 | 0 |  | YES |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_policy_category_subscription](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_policy_category_subscription.md)
- [msdb: dbo.sp_syspolicy_delete_policy_category_subscription](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_policy_category_subscription.md)
- [msdb: dbo.sp_syspolicy_purge_history](../../StoredProcedures/msdb/dbo.sp_syspolicy_purge_history.md)
- [msdb: dbo.sp_syspolicy_update_policy_category_subscription](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_policy_category_subscription.md)

