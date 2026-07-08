# dbo.export_great_plains_ar_vw

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.export_great_plains_ar_vw"]
    dbo_export_great_plains_ar(["dbo.export_great_plains_ar"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.export_great_plains_ar |

## View Code

```sql
create view dbo.export_great_plains_ar_vw  AS
SELECT record_content
FROM dbo.export_great_plains_ar
```

