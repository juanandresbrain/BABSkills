# dbo.dw_rebuild_request

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_rebuild_request"]
    dbo_rebuild_request(["dbo.rebuild_request"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.rebuild_request |

## View Code

```sql
CREATE VIEW dbo.dw_rebuild_request AS
SELECT request_id,
       rebuild_type,
       request_datetime,
       user_name,
       rebuild_from_date,
       rebuild_to_date,
       rebuild_from_store,
       rebuild_to_store,
       tax_jurisdiction,
       user_id,
       copied_from_request_id
  FROM dbo.rebuild_request
```

