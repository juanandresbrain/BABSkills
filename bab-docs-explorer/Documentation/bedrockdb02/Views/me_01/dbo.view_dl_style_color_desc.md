# dbo.view_dl_style_color_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_color_desc"]
    dbo_dl_style_color_desc(["dbo.dl_style_color_desc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_color_desc |

## View Code

```sql
create view dbo.view_dl_style_color_desc AS
SELECT dl_style_color_desc_id,
   record_no,
   style_code,
   color_code,
   locale_identifier,
   long_desc,
   short_desc
FROM dl_style_color_desc
```

