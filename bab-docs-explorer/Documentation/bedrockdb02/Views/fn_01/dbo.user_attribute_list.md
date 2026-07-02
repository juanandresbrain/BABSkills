# dbo.user_attribute_list

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_attribute_list"]
    dbo_FNDTN_SCRTY_USER_ATRBT_LIST(["dbo.FNDTN_SCRTY_USER_ATRBT_LIST"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_USER_ATRBT_LIST |

## View Code

```sql
create view  dbo.user_attribute_list (user_id,user_attrib_id,user_attrib_value)
AS SELECT USER_ID,USER_ATRBT_ID,USER_ATRBT_VAL
FROM dbo.FNDTN_SCRTY_USER_ATRBT_LIST
```

