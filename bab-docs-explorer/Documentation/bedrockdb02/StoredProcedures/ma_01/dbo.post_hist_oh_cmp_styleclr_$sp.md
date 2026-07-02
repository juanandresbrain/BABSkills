# dbo.post_hist_oh_cmp_styleclr_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_oh_cmp_styleclr_$sp"]
    dbo_post_hist_cmp_styleclr(["dbo.post_hist_cmp_styleclr"]) --> SP
    dbo_post_hist_oh_styleclr(["dbo.post_hist_oh_styleclr"]) --> SP
    dbo_post_hist_styleclr(["dbo.post_hist_styleclr"]) --> SP
    dbo_post_hist_styleclr_sum(["dbo.post_hist_styleclr_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.post_hist_cmp_styleclr |
| dbo.post_hist_oh_styleclr |
| dbo.post_hist_styleclr |
| dbo.post_hist_styleclr_sum |

## Stored Procedure Code

```sql

```

