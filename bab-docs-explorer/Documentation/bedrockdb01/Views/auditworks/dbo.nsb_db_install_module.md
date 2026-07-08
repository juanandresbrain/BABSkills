# dbo.nsb_db_install_module

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.nsb_db_install_module"]
    dbo_db_install_module(["dbo.db_install_module"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.db_install_module |

## View Code

```sql
CREATE VIEW [dbo].[nsb_db_install_module] (execution_id, module_id, module_name, from_release_no, from_build_no, to_release_no, to_build_no, execution_status) AS SELECT execution_id, module_id, module_name, from_release_no, from_build_no, to_release_no, to_build_no, execution_status FROM [dbo].[db_install_module]
```

