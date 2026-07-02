# dbo.user_attribute

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_attribute"]
    dbo_FNDTN_SCRTY_USER_ATRBT(["dbo.FNDTN_SCRTY_USER_ATRBT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_USER_ATRBT |

## View Code

```sql
create view  dbo.user_attribute 
(user_attrib_id,user_attrib_name,user_attrib_description,user_attrib_mask,user_attrib_cliptext,user_attrib_required)
AS SELECT USER_ATRBT_ID,USER_ATRBT_NAME,USER_ATRBT_DESC,USER_ATRBT_MASK,USER_ATRBT_CLIP_TEXT,USER_ATRBT_RQRD
FROM dbo.FNDTN_SCRTY_USER_ATRBT
```

