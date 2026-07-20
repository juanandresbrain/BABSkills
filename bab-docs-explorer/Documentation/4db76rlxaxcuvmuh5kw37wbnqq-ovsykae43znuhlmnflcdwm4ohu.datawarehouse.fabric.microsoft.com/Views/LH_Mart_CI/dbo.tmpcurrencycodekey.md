# dbo.tmpcurrencycodekey

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpcurrencycodekey"]
    dbo_tmpcurrencycodekey(["dbo.tmpcurrencycodekey"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpcurrencycodekey |

## View Code

```sql
; CREATE   VIEW tmpcurrencycodekey AS SELECT * FROM LH_Mart.dbo.tmpcurrencycodekey;
```

