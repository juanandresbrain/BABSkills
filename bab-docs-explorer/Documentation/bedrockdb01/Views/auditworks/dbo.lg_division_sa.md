# dbo.lg_division_sa

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_division_sa"]
    language_dependent_description(["language_dependent_description"]) --> VIEW
    security_user(["security_user"]) --> VIEW
    user_division(["user_division"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| language_dependent_description |
| security_user |
| user_division |

## View Code

```sql
create view dbo.lg_division_sa           

 
AS
    SELECT division_code, IsNull(ld.display_description, division_name) as division_name 
      FROM user_division s, security_user u, language_dependent_description ld
where u.user_id = suser_sname() and s.resource_id *= ld.resource_id and u.language_id *= ld.language_id
```

