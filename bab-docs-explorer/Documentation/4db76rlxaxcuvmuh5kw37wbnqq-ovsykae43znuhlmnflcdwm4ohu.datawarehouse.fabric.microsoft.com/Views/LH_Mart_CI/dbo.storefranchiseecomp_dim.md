# dbo.storefranchiseecomp_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.storefranchiseecomp_dim"]
    dbo_storefranchiseecomp_dim(["dbo.storefranchiseecomp_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.storefranchiseecomp_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[storefranchiseecomp_dim] AS     SELECT [recID], [store_key], [date_key_from], [date_key_thru]     FROM [dbo].[storefranchiseecomp_dim]
```

