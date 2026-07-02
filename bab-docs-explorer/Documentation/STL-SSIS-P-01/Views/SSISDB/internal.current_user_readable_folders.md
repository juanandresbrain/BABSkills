# internal.current_user_readable_folders

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["internal.current_user_readable_folders"]
    catalog_effective_object_permissions(["catalog.effective_object_permissions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| catalog.effective_object_permissions |

## View Code

```sql
CREATE VIEW [internal].[current_user_readable_folders]
AS
SELECT     [object_id] AS [ID]
FROM       [catalog].[effective_object_permissions]
WHERE      [object_type] = 1
           AND  [permission_type] = 1
```

