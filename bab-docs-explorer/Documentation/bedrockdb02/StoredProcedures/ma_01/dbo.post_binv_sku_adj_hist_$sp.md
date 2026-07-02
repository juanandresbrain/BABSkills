# dbo.post_binv_sku_adj_hist_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_sku_adj_hist_$sp"]
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> SP
    dbo_post_binv_sku_adj(["dbo.post_binv_sku_adj"]) --> SP
    dbo_post_binv_sku_sum(["dbo.post_binv_sku_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_sku_loc_wk |
| dbo.post_binv_sku_adj |
| dbo.post_binv_sku_sum |

## Stored Procedure Code

```sql

```

