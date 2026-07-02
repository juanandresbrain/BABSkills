# dbo.view_style_location_color_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_location_color_cs"]
    dbo_style_location_color(["dbo.style_location_color"]) --> VIEW
    dbo_style_location_color_cs(["dbo.style_location_color_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_location_color |
| dbo.style_location_color_cs |

## View Code

```sql
create view dbo.view_style_location_color_cs 
AS
SELECT [style_location_color_id]
      ,[style_id]
      ,[location_id]
      ,[style_color_id]
      ,[jurisdiction_id]
      ,[original_selling_retail]
      ,[original_valuation_retail]
      ,[original_price_status_id]
      ,[current_selling_retail]
      ,[current_valuation_retail]
      ,[current_price_status_id]
      ,[mix_match_rule_id1]
      ,[mix_match_rule_id2]
      ,[mix_match_rule_id3]
      ,[mix_match_rule_id4]
  FROM [style_location_color]
UNION ALL
SELECT [style_location_color_id]
      ,[style_id]
      ,[location_id]
      ,[style_color_id]
      ,[jurisdiction_id]
      ,[original_selling_retail]
      ,[original_valuation_retail]
      ,[original_price_status_id]
      ,[current_selling_retail]
      ,[current_valuation_retail]
      ,[current_price_status_id]
      ,[mix_match_rule_id1]
      ,[mix_match_rule_id2]
      ,[mix_match_rule_id3]
      ,[mix_match_rule_id4]
  FROM [style_location_color_cs]
```

