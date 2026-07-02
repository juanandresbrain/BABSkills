# dbo.syspolicy_policy_categories_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| policy_category_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| mandate_database_subscriptions | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_add_policy_category](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_policy_category.md)
- [msdb: dbo.sp_syspolicy_add_policy_category_subscription](../../StoredProcedures/msdb/dbo.sp_syspolicy_add_policy_category_subscription.md)
- [msdb: dbo.sp_syspolicy_delete_policy_category](../../StoredProcedures/msdb/dbo.sp_syspolicy_delete_policy_category.md)
- [msdb: dbo.sp_syspolicy_update_policy_category_subscription](../../StoredProcedures/msdb/dbo.sp_syspolicy_update_policy_category_subscription.md)

