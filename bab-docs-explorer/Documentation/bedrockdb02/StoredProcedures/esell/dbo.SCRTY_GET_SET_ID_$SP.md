# dbo.SCRTY_GET_SET_ID_$SP

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SCRTY_GET_SET_ID_$SP"]
    dbo_ORG_CHN_HRCHY_APP(["dbo.ORG_CHN_HRCHY_APP"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP(["dbo.ORG_CHN_HRCHY_LVL_GRP"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SET_A(["dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A"]) --> SP
    dbo_ORG_CHN_HRCHY_LVL_GRP_SUBSET(["dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET"]) --> SP
    dbo_SCRTY_GET_SET_FMLY_ID__SP(["dbo.SCRTY_GET_SET_FMLY_ID_$SP"]) --> SP
    dbo_SCRTY_MNT_POP_ALL_SUBSETS__SP(["dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP"]) --> SP
    dbo_SCRTY_MNT_POP_FMLY_INTRSCT__SP(["dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP"]) --> SP
    dbo_SCRTY_MNT_POP_SET_SUBSETS__SP(["dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY_APP |
| dbo.ORG_CHN_HRCHY_LVL_GRP |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SET_A |
| dbo.ORG_CHN_HRCHY_LVL_GRP_SUBSET |
| dbo.SCRTY_GET_SET_FMLY_ID_$SP |
| dbo.SCRTY_MNT_POP_ALL_SUBSETS_$SP |
| dbo.SCRTY_MNT_POP_FMLY_INTRSCT_$SP |
| dbo.SCRTY_MNT_POP_SET_SUBSETS_$SP |

## Stored Procedure Code

```sql

```

