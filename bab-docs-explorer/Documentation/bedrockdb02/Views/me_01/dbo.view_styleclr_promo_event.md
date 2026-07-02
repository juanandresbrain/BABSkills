# dbo.view_styleclr_promo_event

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_styleclr_promo_event"]
    dbo_color(["dbo.color"]) --> VIEW
    dbo_promotional_event(["dbo.promotional_event"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.color |
| dbo.promotional_event |
| dbo.style |
| dbo.style_color |

## View Code

```sql
create view dbo.view_styleclr_promo_event AS
SELECT DISTINCT
  sc.style_color_id, 
  sc.style_id,
  s.style_code,
  s.long_desc,
  s.short_desc,
  sc.long_desc style_color_long_desc, 
  sc.short_desc style_color_short_desc,
  c.color_code,
  c.color_long_description,
  c.color_short_description
FROM  style s
INNER JOIN style_color sc
ON s.style_id = sc.style_id
INNER JOIN color c
ON sc.color_id = c.color_id
WHERE sc.style_color_id in (SELECT DISTINCT style_color_id FROM promotional_event)
```

