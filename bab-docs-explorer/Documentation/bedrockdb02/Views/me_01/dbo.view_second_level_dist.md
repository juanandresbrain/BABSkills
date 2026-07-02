# dbo.view_second_level_dist

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_second_level_dist"]
    dbo_distribution(["dbo.distribution"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution |

## View Code

```sql
create view dbo.view_second_level_dist AS

SELECT distribution_id, CAST(0 AS bit) second_level_distribution 
FROM distribution
WHERE parent_distribution_id IS NULL
UNION ALL
SELECT distribution_id, CAST(1 AS bit) second_level_distribution 
FROM distribution
WHERE parent_distribution_id IS NOT NULL
```

