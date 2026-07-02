# dbo.view_dl_style_attachment

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_attachment"]
    dbo_dl_style_attachment(["dbo.dl_style_attachment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_attachment |

## View Code

```sql
create view dbo.view_dl_style_attachment AS
SELECT dl_style_attachment_id,
   record_no,
   style_code,
   attachment_type_code,
   attachment_desc,
   attachment_date,
   primary_flag,
   url
FROM dl_style_attachment
```

