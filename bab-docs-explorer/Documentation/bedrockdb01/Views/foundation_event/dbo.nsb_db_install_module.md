# dbo.nsb_db_install_module

**Database:** foundation_event  
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
CREATE VIEW [dbo].[nsb_db_install_module] (execution_id
```

