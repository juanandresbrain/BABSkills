# dbo.franchiseetransactioninvalidstores

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactioninvalidstores"]
    dbo_franchiseetransactioninvalidstores(["dbo.franchiseetransactioninvalidstores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactioninvalidstores |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactioninvalidstores] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDateTime], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID] FROM [dbo].[franchiseetransactioninvalidstores]
```

