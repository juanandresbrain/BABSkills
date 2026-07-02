# dbo.post_flsh_ent_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_flsh_ent_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_hist_flsh_chn_da(["dbo.hist_flsh_chn_da"]) --> SP
    dbo_hist_flsh_loc_da(["dbo.hist_flsh_loc_da"]) --> SP
    dbo_post_flsh_ent_sum(["dbo.post_flsh_ent_sum"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.hist_flsh_chn_da |
| dbo.hist_flsh_loc_da |
| dbo.post_flsh_ent_sum |

## Stored Procedure Code

```sql

```

