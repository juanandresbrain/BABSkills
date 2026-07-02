# dbo.roll_oh_sku_yr_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.roll_oh_sku_yr_$sp"]
    dbo_hist_oh_sku_chn_yr(["dbo.hist_oh_sku_chn_yr"]) --> SP
    dbo_hist_oh_sku_loc_yr(["dbo.hist_oh_sku_loc_yr"]) --> SP
    dbo_post_roll_oh_yr(["dbo.post_roll_oh_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_sku_chn_yr |
| dbo.hist_oh_sku_loc_yr |
| dbo.post_roll_oh_yr |

## Stored Procedure Code

```sql

```

