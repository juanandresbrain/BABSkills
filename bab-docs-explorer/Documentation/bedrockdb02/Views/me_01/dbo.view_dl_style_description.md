# dbo.view_dl_style_description

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_description"]
    dbo_dl_style_description(["dbo.dl_style_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_description |

## View Code

```sql
create view dbo.view_dl_style_description AS
SELECT dl_style_description_id,
   record_no,
   style_code,
   locale_identifier,
   long_desc,
   short_desc,
   plu_desc
FROM dl_style_description
```

