# dbo.sa_res_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sa_res_detail"]
    dbo_FNDTN_RES_DETAIL(["dbo.FNDTN_RES_DETAIL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_RES_DETAIL |

## View Code

```sql
create view dbo.sa_res_detail AS
SELECT RESOURCE_ID resource_id,
       CULTURE_LCID culture_lcid,
       IS_USER is_user,
       RESOURCE_VALUE resource_value FROM foundation.dbo.FNDTN_RES_DETAIL
```

