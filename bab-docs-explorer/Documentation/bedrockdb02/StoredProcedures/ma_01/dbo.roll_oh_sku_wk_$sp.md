# dbo.roll_oh_sku_wk_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.roll_oh_sku_wk_$sp"]
    dbo_hist_oh_sku_chn_wk(["dbo.hist_oh_sku_chn_wk"]) --> SP
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> SP
    dbo_post_roll_oh_wk(["dbo.post_roll_oh_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_sku_chn_wk |
| dbo.hist_oh_sku_loc_wk |
| dbo.post_roll_oh_wk |

## Stored Procedure Code

```sql

```

