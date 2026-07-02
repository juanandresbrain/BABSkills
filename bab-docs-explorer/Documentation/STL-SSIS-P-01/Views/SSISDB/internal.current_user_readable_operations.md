# internal.current_user_readable_operations

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["internal.current_user_readable_operations"]
    catalog_effective_object_permissions(["catalog.effective_object_permissions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| catalog.effective_object_permissions |

## View Code

```sql
CREATE VIEW [internal].[current_user_readable_operations]
AS
SELECT     [object_id] AS [ID]
FROM       [catalog].[effective_object_permissions]
WHERE      [object_type] = 4
           AND  [permission_type] = 1
```

