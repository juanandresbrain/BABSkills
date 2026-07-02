# dbo.hk_style_reclass_oo_all_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_reclass_oo_all_$sp"]
    dbo_oo_all_style_loc_wk(["dbo.oo_all_style_loc_wk"]) --> SP
    dbo_post_oo_all_group_sum(["dbo.post_oo_all_group_sum"]) --> SP
    dbo_post_oo_all_style_sum(["dbo.post_oo_all_style_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.oo_all_style_loc_wk |
| dbo.post_oo_all_group_sum |
| dbo.post_oo_all_style_sum |

## Stored Procedure Code

```sql

```

