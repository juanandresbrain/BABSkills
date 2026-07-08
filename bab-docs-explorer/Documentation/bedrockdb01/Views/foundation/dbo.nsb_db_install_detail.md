# dbo.nsb_db_install_detail

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.nsb_db_install_detail"]
    dbo_db_install_detail(["dbo.db_install_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.db_install_detail |

## View Code

```sql
CREATE VIEW [dbo].[nsb_db_install_detail] (execution_id, module_id, object_version_id, object_name, object_type_name, execution_status, error_message) AS SELECT execution_id, module_id, object_version_id, object_name, object_type_name, execution_status, error_message FROM [dbo].[db_install_detail]
```

