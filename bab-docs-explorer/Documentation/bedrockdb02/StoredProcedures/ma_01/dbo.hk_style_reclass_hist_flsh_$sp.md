# dbo.hk_style_reclass_hist_flsh_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_reclass_hist_flsh_$sp"]
    dbo_hist_flsh_style_loc_da(["dbo.hist_flsh_style_loc_da"]) --> SP
    dbo_post_flsh_group_sum(["dbo.post_flsh_group_sum"]) --> SP
    dbo_post_flsh_style_sum(["dbo.post_flsh_style_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_flsh_style_loc_da |
| dbo.post_flsh_group_sum |
| dbo.post_flsh_style_sum |

## Stored Procedure Code

```sql

```

