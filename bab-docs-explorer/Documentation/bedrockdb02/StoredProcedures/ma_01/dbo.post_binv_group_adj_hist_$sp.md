# dbo.post_binv_group_adj_hist_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_group_adj_hist_$sp"]
    dbo_hist_oh_group_loc_wk(["dbo.hist_oh_group_loc_wk"]) --> SP
    dbo_post_binv_group_adj(["dbo.post_binv_group_adj"]) --> SP
    dbo_post_binv_group_sum(["dbo.post_binv_group_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_group_loc_wk |
| dbo.post_binv_group_adj |
| dbo.post_binv_group_sum |

## Stored Procedure Code

```sql
CREATE proc [dbo].[post_binv_group_adj_hist_$sp]
```

