# dbo.view_dl_style_location_color

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_location_color"]
    dbo_dl_style_location_color(["dbo.dl_style_location_color"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_location_color |

## View Code

```sql
create view dbo.view_dl_style_location_color AS
SELECT dl_style_location_color_id,
   record_no,
   style_code,
   location_code,
   color_code,
   original_selling_retail,
   original_price_status_code,
   current_selling_retail,
   current_price_status_code,
   mix_match_rule_code1,
   mix_match_rule_code2,
   mix_match_rule_code3,
   mix_match_rule_code4
FROM dl_style_location_color
```

