# dbo.syspolicy_policy_execution_history_details

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syspolicy_policy_execution_history_details"]
    dbo_syspolicy_policy_execution_history_details_internal(["dbo.syspolicy_policy_execution_history_details_internal"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syspolicy_policy_execution_history_details_internal |

## View Code

```sql
CREATE VIEW [dbo].[syspolicy_policy_execution_history_details]
AS
    SELECT 
        detail_id,
        history_id,
        target_query_expression,
        execution_date,
        result,
        result_detail,
        exception_message,
        exception
    FROM [dbo].[syspolicy_policy_execution_history_details_internal]
```

