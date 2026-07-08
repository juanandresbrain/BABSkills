# dbo.dw_period_end_status

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_period_end_status"]
    period_end_status(["period_end_status"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| period_end_status |

## View Code

```sql
CREATE VIEW dbo.dw_period_end_status AS
SELECT instance_id,
       process_start_time,
       process_end_time,
       period_end_status
  FROM period_end_status
```

