# dbo.tmp_franchiseefilesimportselecttransactionpaymentinsert_ae

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselecttransactionpaymentinsert_ae"]
    dbo_tmp_franchiseefilesimportselecttransactionpaymentinsert_ae(["dbo.tmp_franchiseefilesimportselecttransactionpaymentinsert_ae"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselecttransactionpaymentinsert_ae |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselecttransactionpaymentinsert_ae] AS SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionPaymentID], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [PaymentType] COLLATE Latin1_General_CI_AS AS [PaymentType], [Amount], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [currency_key], [UpdateDate] FROM [dbo].[tmp_franchiseefilesimportselecttransactionpaymentinsert_ae]
```

