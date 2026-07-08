# dbo.lg_feature

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_feature"]
    feature(["feature"]) --> VIEW
    language_dependent_description(["language_dependent_description"]) --> VIEW
    security_user(["security_user"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| feature |
| language_dependent_description |
| security_user |

## View Code

```sql
create view dbo.lg_feature 

   AS SELECT entity
,s.feature_code
,IsNull(ld.display_description, feature_description) as feature_description
,feature_code_group
,timestamp
,last_audit_datetime
,s.resource_id
FROM  feature s
INNER JOIN security_user u ON (u.user_id = suser_sname())
LEFT JOIN language_dependent_description ld ON (s.resource_id = ld.resource_id AND u.language_id = ld.language_id)
```

