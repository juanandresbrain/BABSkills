# dbo.post_wrk_ib_inventory_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_wrk_ib_inventory_$sp"]
    dbo_is_tax_exclusive__sp(["dbo.is_tax_exclusive_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_syn_ib_inventory(["dbo.syn_ib_inventory"]) --> SP
    dbo_syn_ib_notax_retail_work(["dbo.syn_ib_notax_retail_work"]) --> SP
    dbo_syn_sku(["dbo.syn_sku"]) --> SP
    dbo_syn_style_color(["dbo.syn_style_color"]) --> SP
    dbo_syn_style_group(["dbo.syn_style_group"]) --> SP
    dbo_syn_style_size(["dbo.syn_style_size"]) --> SP
    dbo_wrk_ib_inventory(["dbo.wrk_ib_inventory"]) --> SP
    dbo_wrk_ib_iv_style_alt_group(["dbo.wrk_ib_iv_style_alt_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.is_tax_exclusive_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.syn_ib_inventory |
| dbo.syn_ib_notax_retail_work |
| dbo.syn_sku |
| dbo.syn_style_color |
| dbo.syn_style_group |
| dbo.syn_style_size |
| dbo.wrk_ib_inventory |
| dbo.wrk_ib_iv_style_alt_group |

## Stored Procedure Code

```sql

```

