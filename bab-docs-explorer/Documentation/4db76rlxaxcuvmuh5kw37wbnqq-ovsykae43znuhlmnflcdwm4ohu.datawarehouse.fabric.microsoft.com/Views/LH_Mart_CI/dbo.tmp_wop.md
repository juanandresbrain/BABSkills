# dbo.tmp_wop

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_wop"]
    dbo_tmp_wop(["dbo.tmp_wop"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_wop |

## View Code

```sql
; CREATE   VIEW tmp_wop AS SELECT * FROM LH_Mart.dbo.tmp_wop;
```

