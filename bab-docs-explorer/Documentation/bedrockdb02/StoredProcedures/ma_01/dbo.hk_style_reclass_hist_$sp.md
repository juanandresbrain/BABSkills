# dbo.hk_style_reclass_hist_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_reclass_hist_$sp"]
    dbo_hist_style_loc_wk(["dbo.hist_style_loc_wk"]) --> SP
    dbo_post_hist_group(["dbo.post_hist_group"]) --> SP
    dbo_post_hist_style(["dbo.post_hist_style"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_style_loc_wk |
| dbo.post_hist_group |
| dbo.post_hist_style |

## Stored Procedure Code

```sql

```

