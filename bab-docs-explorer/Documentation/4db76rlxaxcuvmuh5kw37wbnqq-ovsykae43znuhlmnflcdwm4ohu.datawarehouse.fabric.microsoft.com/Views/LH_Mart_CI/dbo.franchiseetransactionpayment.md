# dbo.franchiseetransactionpayment

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionpayment"]
    dbo_franchiseetransactionpayment(["dbo.franchiseetransactionpayment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionpayment |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionpayment] AS     SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionPaymentID], [PaymentType] COLLATE Latin1_General_CI_AS AS [PaymentType], [Amount], [InsertDate], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID], [currency_key], [UpdateDate]     FROM [dbo].[franchiseetransactionpayment]
```

