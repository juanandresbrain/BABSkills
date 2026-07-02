# dbo.post_oo_all_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oo_all_sku_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_oo_all_sku_chn_li(["dbo.oo_all_sku_chn_li"]) --> SP
    dbo_oo_all_sku_chn_pd(["dbo.oo_all_sku_chn_pd"]) --> SP
    dbo_oo_all_sku_chn_wk(["dbo.oo_all_sku_chn_wk"]) --> SP
    dbo_oo_all_sku_chn_yr(["dbo.oo_all_sku_chn_yr"]) --> SP
    dbo_oo_all_sku_loc_li(["dbo.oo_all_sku_loc_li"]) --> SP
    dbo_oo_all_sku_loc_pd(["dbo.oo_all_sku_loc_pd"]) --> SP
    dbo_oo_all_sku_loc_wk(["dbo.oo_all_sku_loc_wk"]) --> SP
    dbo_oo_all_sku_loc_yr(["dbo.oo_all_sku_loc_yr"]) --> SP
    dbo_post_oo_all_sku_sum(["dbo.post_oo_all_sku_sum"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.calendar_merch_week |
| dbo.oo_all_sku_chn_li |
| dbo.oo_all_sku_chn_pd |
| dbo.oo_all_sku_chn_wk |
| dbo.oo_all_sku_chn_yr |
| dbo.oo_all_sku_loc_li |
| dbo.oo_all_sku_loc_pd |
| dbo.oo_all_sku_loc_wk |
| dbo.oo_all_sku_loc_yr |
| dbo.post_oo_all_sku_sum |
| dbo.sku |

## Stored Procedure Code

```sql

```

