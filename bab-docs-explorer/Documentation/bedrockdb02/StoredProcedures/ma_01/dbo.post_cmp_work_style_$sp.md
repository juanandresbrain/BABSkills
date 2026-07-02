# dbo.post_cmp_work_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_cmp_work_style_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_component_xref(["dbo.component_xref"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_post_cmp_work_style(["dbo.post_cmp_work_style"]) --> SP
    dbo_post_hist_cmp_style(["dbo.post_hist_cmp_style"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.component_xref |
| dbo.history_component |
| dbo.post_cmp_work_style |
| dbo.post_hist_cmp_style |

## Stored Procedure Code

```sql

```

