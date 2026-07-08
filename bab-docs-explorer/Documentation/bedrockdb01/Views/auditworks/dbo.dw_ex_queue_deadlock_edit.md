# dbo.dw_ex_queue_deadlock_edit

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_ex_queue_deadlock_edit"]
    dbo_ex_queue_deadlock_edit(["dbo.ex_queue_deadlock_edit"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ex_queue_deadlock_edit |

## View Code

```sql
CREATE VIEW dbo.dw_ex_queue_deadlock_edit AS
SELECT stream_number
  FROM dbo.ex_queue_deadlock_edit
```

