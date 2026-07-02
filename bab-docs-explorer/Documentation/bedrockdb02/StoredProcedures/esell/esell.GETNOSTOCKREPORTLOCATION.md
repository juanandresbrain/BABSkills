# esell.GETNOSTOCKREPORTLOCATION

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.GETNOSTOCKREPORTLOCATION"]
    dbo_batch_no_stock_location(["dbo.batch_no_stock_location"]) --> SP
    dbo_batch_no_stock_t_location(["dbo.batch_no_stock_t_location"]) --> SP
    dbo_fGetDelimitedAttributeValues(["dbo.fGetDelimitedAttributeValues"]) --> SP
    dbo_fGetDelimitedLocationValues(["dbo.fGetDelimitedLocationValues"]) --> SP
    dbo_fGetDelimitedNoStockReasonIds(["dbo.fGetDelimitedNoStockReasonIds"]) --> SP
    dbo_GETHIERARCHYLOCATIONLIST(["dbo.GETHIERARCHYLOCATIONLIST"]) --> SP
    dbo_GETLOCATIONATTRIBUTELIST(["dbo.GETLOCATIONATTRIBUTELIST"]) --> SP
    dbo_Org_Chn_Hrchy_Lvl(["dbo.Org_Chn_Hrchy_Lvl"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP(["dbo.ORG_CHN_HRCHY_LVL_GRP"]) --> SP
    dbo_Org_Chn_Hrchy_Lvl_Grp_A(["dbo.Org_Chn_Hrchy_Lvl_Grp_A"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_no_stock_location |
| dbo.batch_no_stock_t_location |
| dbo.fGetDelimitedAttributeValues |
| dbo.fGetDelimitedLocationValues |
| dbo.fGetDelimitedNoStockReasonIds |
| dbo.GETHIERARCHYLOCATIONLIST |
| dbo.GETLOCATIONATTRIBUTELIST |
| dbo.Org_Chn_Hrchy_Lvl |
| dbo.ORG_CHN_HRCHY_LVL_GRP |
| dbo.Org_Chn_Hrchy_Lvl_Grp_A |

## Stored Procedure Code

```sql

```

