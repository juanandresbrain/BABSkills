# dbo.post_cmp_work_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_cmp_work_sku_$sp"]
    dbo_component_xref(["dbo.component_xref"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_post_cmp_work_sku(["dbo.post_cmp_work_sku"]) --> SP
    dbo_post_hist_cmp_sku(["dbo.post_hist_cmp_sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.component_xref |
| dbo.history_component |
| dbo.post_cmp_work_sku |
| dbo.post_hist_cmp_sku |

## Stored Procedure Code

```sql

```

