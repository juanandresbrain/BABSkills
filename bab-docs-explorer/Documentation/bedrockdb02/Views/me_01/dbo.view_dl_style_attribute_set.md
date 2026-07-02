# dbo.view_dl_style_attribute_set

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_attribute_set"]
    dbo_dl_style_attribute_set(["dbo.dl_style_attribute_set"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_attribute_set |

## View Code

```sql
create view dbo.view_dl_style_attribute_set AS
SELECT dl_style_attribute_set_id,
   record_no,
   action_type,
   style_code,
   attribute_code,
   attribute_set_code
FROM dl_style_attribute_set
```

