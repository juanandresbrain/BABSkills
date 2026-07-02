# dbo.view_dl_style_vendor

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_vendor"]
    dbo_dl_style_vendor(["dbo.dl_style_vendor"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_vendor |

## View Code

```sql
create view dbo.view_dl_style_vendor AS
SELECT dl_style_vendor_id,
   record_no,
   style_code,
   vendor_code,
   vendor_style,
   current_cost,
   currency_code
FROM dl_style_vendor
```

