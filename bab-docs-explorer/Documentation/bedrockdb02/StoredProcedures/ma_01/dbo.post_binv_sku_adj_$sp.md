# dbo.post_binv_sku_adj_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_sku_adj_$sp"]
    dbo_j(["dbo.j"]) --> SP
    dbo_post_binv_sku_adj(["dbo.post_binv_sku_adj"]) --> SP
    dbo_post_binv_sku_sum(["dbo.post_binv_sku_sum"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.j |
| dbo.post_binv_sku_adj |
| dbo.post_binv_sku_sum |
| dbo.sku |

## Stored Procedure Code

```sql

```

