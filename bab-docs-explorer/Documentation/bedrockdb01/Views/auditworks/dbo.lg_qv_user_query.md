# dbo.lg_qv_user_query

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_qv_user_query"]
    language_dependent_description(["language_dependent_description"]) --> VIEW
    qv_user_query(["qv_user_query"]) --> VIEW
    security_user(["security_user"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| language_dependent_description |
| qv_user_query |
| security_user |

## View Code

```sql
create view dbo.lg_qv_user_query 
as

SELECT query_id
,name
,IsNull(ld.display_description, description) as description
,created_by
,user_stored_proc
,s.resource_id
FROM qv_user_query s
     INNER JOIN security_user u
        ON u.user_id = suser_sname()
      LEFT OUTER JOIN language_dependent_description ld 
        ON s.resource_id = ld.resource_id
       AND u.language_id = ld.language_id
```

