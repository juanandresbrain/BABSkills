# catalog.customized_logging_levels

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["catalog.customized_logging_levels"]
    internal_customized_logging_levels(["internal.customized_logging_levels"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| internal.customized_logging_levels |

## View Code

```sql
CREATE VIEW [catalog].[customized_logging_levels]
AS
SELECT     [level_id],
           [name],
           [description],
           [profile_value],
           [events_value],
           [created_by_sid],
           [created_by_name],
           [created_time]
FROM       [internal].[customized_logging_levels]
```

