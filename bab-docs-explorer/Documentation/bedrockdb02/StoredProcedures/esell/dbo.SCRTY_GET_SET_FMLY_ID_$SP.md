# dbo.SCRTY_GET_SET_FMLY_ID_$SP

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SCRTY_GET_SET_FMLY_ID_$SP"]
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET_F_A(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_A"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET_F_I(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_I"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET_FMLY(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET_FMLY"]) --> SP
    dbo_SCRTY_MNT_POP_FMLY_INTRSCT__SP(["dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_A |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET_F_I |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET_FMLY |
| dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP |

## Stored Procedure Code

```sql

```

