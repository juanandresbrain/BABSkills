# dbo.franchiseetransactionpaymenterror

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionpaymenterror"]
    dbo_franchiseetransactionpaymenterror(["dbo.franchiseetransactionpaymenterror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionpaymenterror |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionpaymenterror] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [PaymentType] COLLATE Latin1_General_CI_AS AS [PaymentType], [Amount] COLLATE Latin1_General_CI_AS AS [Amount], [InsertDate] COLLATE Latin1_General_CI_AS AS [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc], [ErrorSource] COLLATE Latin1_General_CI_AS AS [ErrorSource] FROM [dbo].[franchiseetransactionpaymenterror]
```

