# dbo.lg_currency_conversion_type

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_currency_conversion_type"]
    currency_conversion_type(["currency_conversion_type"]) --> VIEW
    language_dependent_description(["language_dependent_description"]) --> VIEW
    security_user(["security_user"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| currency_conversion_type |
| language_dependent_description |
| security_user |

## View Code

```sql
create view dbo.lg_currency_conversion_type 
as

SELECT currency_conversion_type_id,
       IsNull(ld.display_description, currency_conversion_type_descr) as currency_conversion_type_descr
FROM currency_conversion_type s
     INNER JOIN security_user u
        ON u.user_id = suser_sname()
      LEFT OUTER JOIN language_dependent_description ld 
        ON s.resource_id = ld.resource_id
       AND u.language_id = ld.language_id
```

