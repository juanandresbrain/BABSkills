# dbo.syspolicy_policy_category_subscriptions_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| policy_category_subscription_id | int | 4 | 0 | YES |  |  |
| target_type | sysname | 256 | 0 |  |  |  |
| target_object | sysname | 256 | 0 |  |  |  |
| policy_category_id | int | 4 | 0 |  | YES |  |

