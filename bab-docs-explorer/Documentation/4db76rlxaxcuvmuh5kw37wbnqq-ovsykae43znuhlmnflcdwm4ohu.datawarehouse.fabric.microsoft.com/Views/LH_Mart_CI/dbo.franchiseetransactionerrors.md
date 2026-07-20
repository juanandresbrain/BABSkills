# dbo.franchiseetransactionerrors

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionerrors"]
    dbo_franchiseetransactionerrors(["dbo.franchiseetransactionerrors"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionerrors |

## View Code

```sql
; CREATE   VIEW franchiseetransactionerrors AS SELECT * FROM LH_Mart.dbo.franchiseetransactionerrors;
```

