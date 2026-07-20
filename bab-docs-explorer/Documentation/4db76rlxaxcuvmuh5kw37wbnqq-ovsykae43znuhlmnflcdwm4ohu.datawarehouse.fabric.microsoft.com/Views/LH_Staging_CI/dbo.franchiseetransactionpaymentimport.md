# dbo.franchiseetransactionpaymentimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionpaymentimport"]
    dbo_franchiseetransactionpaymentimport(["dbo.franchiseetransactionpaymentimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionpaymentimport |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionpaymentimport] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [PaymentType] COLLATE Latin1_General_CI_AS AS [PaymentType], [Amount], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee] FROM [dbo].[franchiseetransactionpaymentimport]
```

