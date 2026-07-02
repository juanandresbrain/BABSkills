# dbo.post_cmp_work_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_cmp_work_group_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_component_xref(["dbo.component_xref"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_post_cmp_work_group(["dbo.post_cmp_work_group"]) --> SP
    dbo_post_hist_cmp_group(["dbo.post_hist_cmp_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.component_xref |
| dbo.history_component |
| dbo.post_cmp_work_group |
| dbo.post_hist_cmp_group |

## Stored Procedure Code

```sql

```

