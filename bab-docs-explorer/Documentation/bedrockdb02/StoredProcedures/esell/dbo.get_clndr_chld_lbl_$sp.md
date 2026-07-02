# dbo.get_clndr_chld_lbl_$sp

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_clndr_chld_lbl_$sp"]
    dbo_CLNDR_LVL_TYPE(["dbo.CLNDR_LVL_TYPE"]) --> SP
    dbo_CLNDR_MNTH_LANG(["dbo.CLNDR_MNTH_LANG"]) --> SP
    dbo_CLNDR_TMPLT_ALGRTHM(["dbo.CLNDR_TMPLT_ALGRTHM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_LVL_TYPE |
| dbo.CLNDR_MNTH_LANG |
| dbo.CLNDR_TMPLT_ALGRTHM |

## Stored Procedure Code

```sql
create proc [dbo].[get_clndr_chld_lbl_$sp]
```

