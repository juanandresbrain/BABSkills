# dbo.lg_currency

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_currency"]
    currency(["currency"]) --> VIEW
    language_dependent_description(["language_dependent_description"]) --> VIEW
    security_user(["security_user"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| currency |
| language_dependent_description |
| security_user |

## View Code

```sql
create view dbo.lg_currency 
as

SELECT currency_id, currency_code,
       IsNull(ld.display_description, currency_description) as currency_description,
       active_flag
FROM currency s
     INNER JOIN security_user u
        ON u.user_id = suser_sname()
      LEFT OUTER JOIN language_dependent_description ld 
        ON s.resource_id = ld.resource_id
       AND u.language_id = ld.language_id
```

