# dbo.tmp_fedex

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_fedex"]
    dbo_tmp_fedex(["dbo.tmp_fedex"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_fedex |

## View Code

```sql
; CREATE   VIEW tmp_fedex AS SELECT * FROM LH_Mart.dbo.tmp_fedex;
```

