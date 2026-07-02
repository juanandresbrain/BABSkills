# dbo.roll_oh_styleclr_pd_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.roll_oh_styleclr_pd_$sp"]
    dbo_hist_oh_styleclr_chn_pd(["dbo.hist_oh_styleclr_chn_pd"]) --> SP
    dbo_hist_oh_styleclr_loc_pd(["dbo.hist_oh_styleclr_loc_pd"]) --> SP
    dbo_post_roll_oh_pd(["dbo.post_roll_oh_pd"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_styleclr_chn_pd |
| dbo.hist_oh_styleclr_loc_pd |
| dbo.post_roll_oh_pd |

## Stored Procedure Code

```sql

```

