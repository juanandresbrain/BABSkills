# dbo.franchiseetransactionpayment

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
;

CREATE VIEW dbo.franchiseetransactionpayment AS SELECT FranchiseeTransactionHeaderID, FranchiseeTransactionPaymentID, PaymentType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PaymentType, Amount, InsertDate, BatchID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BatchID, currency_key, UpdateDate FROM LH_Mart.dbo.franchiseetransactionpayment;;
```

