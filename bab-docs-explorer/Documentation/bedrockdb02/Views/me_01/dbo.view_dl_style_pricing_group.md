# dbo.view_dl_style_pricing_group

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_pricing_group"]
    dbo_dl_style_pricing_group(["dbo.dl_style_pricing_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_pricing_group |

## View Code

```sql
create view dbo.view_dl_style_pricing_group AS
SELECT dl_style_pricing_group_id,
   record_no,
   style_code,
   pricing_group_code,
   original_selling_retail,
   original_price_status_code,
   current_selling_retail,
   current_price_status_code,
   mix_match_rule_code1,
   mix_match_rule_code2,
   mix_match_rule_code3,
   mix_match_rule_code4
FROM dl_style_pricing_group
```

