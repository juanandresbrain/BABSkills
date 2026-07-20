# dbo.franchiseetransactionheadererror

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionheadererror"]
    dbo_franchiseetransactionheadererror(["dbo.franchiseetransactionheadererror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionheadererror |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionheadererror] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDateTime] COLLATE Latin1_General_CI_AS AS [TransactionDateTime], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InsertDate] COLLATE Latin1_General_CI_AS AS [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc], [ErrorSource] COLLATE Latin1_General_CI_AS AS [ErrorSource] FROM [dbo].[franchiseetransactionheadererror]
```

