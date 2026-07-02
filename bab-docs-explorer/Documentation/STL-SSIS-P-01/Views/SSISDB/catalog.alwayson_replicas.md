# catalog.alwayson_replicas

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["catalog.alwayson_replicas"]
    internal_alwayson_support_state(["internal.alwayson_support_state"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| internal.alwayson_support_state |

## View Code

```sql
CREATE VIEW [catalog].[alwayson_replicas] 
AS
SELECT		[server_name],
			[state]
FROM		[internal].[alwayson_support_state]
```

