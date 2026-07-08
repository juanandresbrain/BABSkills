# dbo.dw_period_end_status

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_period_end_status"]
    dbo_period_end_status(["dbo.period_end_status"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.period_end_status |

## View Code

```sql
CREATE VIEW dbo.dw_period_end_status AS
SELECT instance_id,
       process_start_time,
       process_end_time,
       period_end_status
  FROM dbo.period_end_status
```

