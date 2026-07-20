# dbo.franchiseetransactiongiftcardimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactiongiftcardimport"]
    dbo_franchiseetransactiongiftcardimport(["dbo.franchiseetransactiongiftcardimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactiongiftcardimport |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactiongiftcardimport] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Units], [GiftCardAmount], [Discount], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[franchiseetransactiongiftcardimport]
```

