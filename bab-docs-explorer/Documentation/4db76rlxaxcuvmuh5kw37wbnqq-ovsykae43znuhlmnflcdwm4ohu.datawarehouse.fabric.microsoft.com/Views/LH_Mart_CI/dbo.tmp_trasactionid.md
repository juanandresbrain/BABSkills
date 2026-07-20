# dbo.tmp_trasactionid

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_trasactionid"]
    dbo_tmp_trasactionid(["dbo.tmp_trasactionid"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_trasactionid |

## View Code

```sql
; CREATE   VIEW tmp_trasactionid AS SELECT * FROM LH_Mart.dbo.tmp_trasactionid;
```

