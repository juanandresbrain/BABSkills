# internal.current_user_readable_projects

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["internal.current_user_readable_projects"]
    catalog_effective_object_permissions(["catalog.effective_object_permissions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| catalog.effective_object_permissions |

## View Code

```sql
CREATE VIEW [internal].[current_user_readable_projects]
AS
SELECT     [object_id] AS [ID]
FROM       [catalog].[effective_object_permissions]
WHERE      [object_type] = 2
           AND  [permission_type] = 1
```

