# dbo.dl_hist_task_imp_trunc_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_hist_task_imp_trunc_$sp"]
    dbo_dl_hist_group(["dbo.dl_hist_group"]) --> SP
    dbo_dl_hist_oh_group(["dbo.dl_hist_oh_group"]) --> SP
    dbo_dl_hist_oh_sku(["dbo.dl_hist_oh_sku"]) --> SP
    dbo_dl_hist_oh_style(["dbo.dl_hist_oh_style"]) --> SP
    dbo_dl_hist_oh_styleclr(["dbo.dl_hist_oh_styleclr"]) --> SP
    dbo_dl_hist_sku(["dbo.dl_hist_sku"]) --> SP
    dbo_dl_hist_style(["dbo.dl_hist_style"]) --> SP
    dbo_dl_hist_styleclr(["dbo.dl_hist_styleclr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_group |
| dbo.dl_hist_oh_group |
| dbo.dl_hist_oh_sku |
| dbo.dl_hist_oh_style |
| dbo.dl_hist_oh_styleclr |
| dbo.dl_hist_sku |
| dbo.dl_hist_style |
| dbo.dl_hist_styleclr |

## Stored Procedure Code

```sql

```

