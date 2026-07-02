# dbo.post_hist_oh_cmp_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_oh_cmp_sku_$sp"]
    dbo_post_hist_cmp_sku(["dbo.post_hist_cmp_sku"]) --> SP
    dbo_post_hist_oh_sku(["dbo.post_hist_oh_sku"]) --> SP
    dbo_post_hist_sku(["dbo.post_hist_sku"]) --> SP
    dbo_post_hist_sku_sum(["dbo.post_hist_sku_sum"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_hist_cmp_sku |
| dbo.post_hist_oh_sku |
| dbo.post_hist_sku |
| dbo.post_hist_sku_sum |
| dbo.sku |

## Stored Procedure Code

```sql

```

