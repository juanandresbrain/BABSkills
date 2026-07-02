# dbo.view_dl_style_retail

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_style_retail"]
    dbo_dl_style_retail(["dbo.dl_style_retail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_retail |

## View Code

```sql
create view dbo.view_dl_style_retail AS
SELECT dl_style_retail_id,
   record_no,
   style_code,
   jurisdiction_code,
   compare_at_retail,
   original_selling_retail,
   original_price_status_code,
   current_selling_retail,
   current_price_status_code,
   mix_match_rule_code1,
   mix_match_rule_code2,
   mix_match_rule_code3,
   mix_match_rule_code4
FROM dl_style_retail
```

