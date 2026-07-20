# dbo.transactionfact

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transactionfact"]
    dbo_transactionfact(["dbo.transactionfact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transactionfact |

## View Code

```sql
; CREATE   VIEW transactionfact AS SELECT * FROM LH_Mart.dbo.transactionfact;
```

