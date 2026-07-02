# dbo.SCRTY_GET_GRPS_IN_SET_$SP

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SCRTY_GET_GRPS_IN_SET_$SP"]
    dbo_ORG_CHN_HRCHY(["dbo.ORG_CHN_HRCHY"]) --> SP
    dbo_ORG_CHN_HRCHY_APP(["dbo.ORG_CHN_HRCHY_APP"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL(["dbo.ORG_CHN_HRCHY_LVL"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP(["dbo.ORG_CHN_HRCHY_LVL_GRP"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_LANG(["dbo.ORG_CHN_HRCHY_LVL_GRP_LANG"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET_A(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY |
| dbo.ORG_CHN_HRCHY_APP |
| dbo.ORG_CHN_HRCHY_LVL |
| dbo.ORG_CHN_HRCHY_LVL_GRP |
| dbo.ORG_CHN_HRCHY_LVL_GRP_LANG |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A |

## Stored Procedure Code

```sql

```

