# dbo.hk_sku_modify_oo_all_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_sku_modify_oo_all_$sp"]
    dbo_oo_all_sku_chn_li(["dbo.oo_all_sku_chn_li"]) --> SP
    dbo_oo_all_sku_chn_pd(["dbo.oo_all_sku_chn_pd"]) --> SP
    dbo_oo_all_sku_chn_wk(["dbo.oo_all_sku_chn_wk"]) --> SP
    dbo_oo_all_sku_chn_yr(["dbo.oo_all_sku_chn_yr"]) --> SP
    dbo_oo_all_sku_loc_li(["dbo.oo_all_sku_loc_li"]) --> SP
    dbo_oo_all_sku_loc_pd(["dbo.oo_all_sku_loc_pd"]) --> SP
    dbo_oo_all_sku_loc_wk(["dbo.oo_all_sku_loc_wk"]) --> SP
    dbo_oo_all_sku_loc_yr(["dbo.oo_all_sku_loc_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.oo_all_sku_chn_li |
| dbo.oo_all_sku_chn_pd |
| dbo.oo_all_sku_chn_wk |
| dbo.oo_all_sku_chn_yr |
| dbo.oo_all_sku_loc_li |
| dbo.oo_all_sku_loc_pd |
| dbo.oo_all_sku_loc_wk |
| dbo.oo_all_sku_loc_yr |

## Stored Procedure Code

```sql

```

