# queryinsights.sql_pool_insights

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["queryinsights.sql_pool_insights"]
    queryinsights_fabric_workloadinsights(["queryinsights.fabric_workloadinsights"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| queryinsights.fabric_workloadinsights |

## View Code

```sql
CREATE VIEW queryinsights.sql_pool_insights AS SELECT sql_pool_name, metric_timestamp AS timestamp, max_resource_percentage, is_optimized_for_reads, current_workspace_capacity, is_pool_under_pressure, CASE WHEN t1.is_optimized_for_reads = 1 THEN t1.cache_cooldown_minutes ELSE NULL END AS cache_cooldown_minutes from queryinsights.fabric_workloadinsights AS t1 WHERE t1.TIMESTAMP > DATEADD(DAY, -30, GETDATE())
```

