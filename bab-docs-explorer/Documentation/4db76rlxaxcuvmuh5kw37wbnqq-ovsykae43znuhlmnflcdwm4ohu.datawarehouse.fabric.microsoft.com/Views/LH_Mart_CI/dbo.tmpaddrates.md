# dbo.tmpaddrates

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpaddrates"]
    dbo_tmpaddrates(["dbo.tmpaddrates"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpaddrates |

## View Code

```sql
; CREATE   VIEW tmpaddrates AS SELECT * FROM LH_Mart.dbo.tmpaddrates;
```

