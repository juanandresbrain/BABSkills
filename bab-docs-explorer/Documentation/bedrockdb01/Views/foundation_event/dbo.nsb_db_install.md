# dbo.nsb_db_install

**Database:** foundation_event  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.nsb_db_install"]
    dbo_db_install(["dbo.db_install"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.db_install |

## View Code

```sql
CREATE VIEW [dbo].[nsb_db_install] (execution_id
```

