# dbo.get_clndr_chld_cnt_$sp

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_clndr_chld_cnt_$sp"]
    dbo_CLNDR_TMPLT_ALGRTHM(["dbo.CLNDR_TMPLT_ALGRTHM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT_ALGRTHM |

## Stored Procedure Code

```sql
create proc [dbo].[get_clndr_chld_cnt_$sp] (@i_seq integer,
```

