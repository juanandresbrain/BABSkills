# dbo.view_dl_style_size_desc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_size_desc"]
    dbo_dl_style_size_desc(["dbo.dl_style_size_desc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_size_desc |

## View Code

```sql
create view dbo.view_dl_style_size_desc AS
SELECT dl_style_size_desc_id,
   record_no,
   style_code,
   size_code,
   locale_identifier,
   ticket_label_override
FROM dl_style_size_desc
```

