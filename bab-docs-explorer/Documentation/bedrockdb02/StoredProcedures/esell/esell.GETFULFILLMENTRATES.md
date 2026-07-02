# esell.GETFULFILLMENTRATES

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["esell.GETFULFILLMENTRATES"]
    dbo_batch_fulfillment_rates(["dbo.batch_fulfillment_rates"]) --> SP
    dbo_fGetDelimitedAttributeValues(["dbo.fGetDelimitedAttributeValues"]) --> SP
    dbo_fGetDelimitedLocationValues(["dbo.fGetDelimitedLocationValues"]) --> SP
    dbo_GETHIERARCHYLOCATIONLIST(["dbo.GETHIERARCHYLOCATIONLIST"]) --> SP
    dbo_GETLOCATIONATTRIBUTELIST(["dbo.GETLOCATIONATTRIBUTELIST"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL(["dbo.ORG_CHN_HRCHY_LVL"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP(["dbo.ORG_CHN_HRCHY_LVL_GRP"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_A(["dbo.ORG_CHN_HRCHY_LVL_GRP_A"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.batch_fulfillment_rates |
| dbo.fGetDelimitedAttributeValues |
| dbo.fGetDelimitedLocationValues |
| dbo.GETHIERARCHYLOCATIONLIST |
| dbo.GETLOCATIONATTRIBUTELIST |
| dbo.ORG_CHN_HRCHY_LVL |
| dbo.ORG_CHN_HRCHY_LVL_GRP |
| dbo.ORG_CHN_HRCHY_LVL_GRP_A |

## Stored Procedure Code

```sql
--START GETFULFILLMENTRATES--
```

