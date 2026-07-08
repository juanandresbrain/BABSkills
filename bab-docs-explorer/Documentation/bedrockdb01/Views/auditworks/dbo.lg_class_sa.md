# dbo.lg_class_sa

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_class_sa"]
    language_dependent_description(["language_dependent_description"]) --> VIEW
    security_user(["security_user"]) --> VIEW
    user_class(["user_class"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| language_dependent_description |
| security_user |
| user_class |

## View Code

```sql
create view dbo.lg_class_sa 
AS

SELECT upc_lookup_division, class_code, 
           class_description = IsNull(ld.display_description, class_description),
           class_short_description = substring(IsNull(ld.display_description, class_description), 1, 12),
           department_code, tax_item_group_id
FROM user_class s
     LEFT JOIN language_dependent_description ld ON (s.resource_id = ld.resource_id)
     RIGHT JOIN security_user u ON (u.language_id = ISNULL(ld.language_id, u.language_id))
WHERE u.user_id = suser_sname()
```

