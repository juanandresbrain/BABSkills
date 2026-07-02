# dbo.sysutility_ucp_mi_cpu_utilizations

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sysutility_ucp_mi_cpu_utilizations"]
    dbo_sysutility_ucp_instances(["dbo.sysutility_ucp_instances"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysutility_ucp_instances |

## View Code

```sql
CREATE VIEW [dbo].[sysutility_ucp_mi_cpu_utilizations]
AS
SELECT svr.Name AS server_instance_name, 
   10 AS under_utilization, 
   CAST(svr.ProcessorUsage AS INT) AS current_utilization, 
   70 AS over_utilization
FROM	msdb.dbo.sysutility_ucp_instances AS svr;
```

