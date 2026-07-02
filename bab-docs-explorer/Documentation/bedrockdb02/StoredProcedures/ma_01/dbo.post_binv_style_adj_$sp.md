# dbo.post_binv_style_adj_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_style_adj_$sp"]
    dbo_post_binv_style_adj(["dbo.post_binv_style_adj"]) --> SP
    dbo_post_binv_style_sum(["dbo.post_binv_style_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_binv_style_adj |
| dbo.post_binv_style_sum |

## Stored Procedure Code

```sql
CREATE proc [dbo].[post_binv_style_adj_$sp]
```

