# dbo.post_binv_group_adj_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_group_adj_$sp"]
    dbo_post_binv_group_adj(["dbo.post_binv_group_adj"]) --> SP
    dbo_post_binv_group_sum(["dbo.post_binv_group_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_binv_group_adj |
| dbo.post_binv_group_sum |

## Stored Procedure Code

```sql
CREATE proc [dbo].[post_binv_group_adj_$sp]
```

