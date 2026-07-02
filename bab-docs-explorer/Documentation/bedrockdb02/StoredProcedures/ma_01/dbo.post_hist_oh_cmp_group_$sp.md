# dbo.post_hist_oh_cmp_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_oh_cmp_group_$sp"]
    dbo_post_hist_cmp_group(["dbo.post_hist_cmp_group"]) --> SP
    dbo_post_hist_group(["dbo.post_hist_group"]) --> SP
    dbo_post_hist_group_sum(["dbo.post_hist_group_sum"]) --> SP
    dbo_post_hist_oh_group(["dbo.post_hist_oh_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_hist_cmp_group |
| dbo.post_hist_group |
| dbo.post_hist_group_sum |
| dbo.post_hist_oh_group |

## Stored Procedure Code

```sql

```

