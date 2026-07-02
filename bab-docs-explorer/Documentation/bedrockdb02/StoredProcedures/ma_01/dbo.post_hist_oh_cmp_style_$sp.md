# dbo.post_hist_oh_cmp_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_oh_cmp_style_$sp"]
    dbo_post_hist_cmp_style(["dbo.post_hist_cmp_style"]) --> SP
    dbo_post_hist_oh_style(["dbo.post_hist_oh_style"]) --> SP
    dbo_post_hist_style(["dbo.post_hist_style"]) --> SP
    dbo_post_hist_style_sum(["dbo.post_hist_style_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_hist_cmp_style |
| dbo.post_hist_oh_style |
| dbo.post_hist_style |
| dbo.post_hist_style_sum |

## Stored Procedure Code

```sql

```

