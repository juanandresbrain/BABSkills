# dbo.view_dl_style_custom_property

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_custom_property"]
    dbo_dl_style_custom_property(["dbo.dl_style_custom_property"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_custom_property |

## View Code

```sql
create view dbo.view_dl_style_custom_property AS
SELECT dl_style_custom_property_id,
   record_no,
   style_code,
   cust_prop_code,
   custom_property_value
FROM dl_style_custom_property
```

