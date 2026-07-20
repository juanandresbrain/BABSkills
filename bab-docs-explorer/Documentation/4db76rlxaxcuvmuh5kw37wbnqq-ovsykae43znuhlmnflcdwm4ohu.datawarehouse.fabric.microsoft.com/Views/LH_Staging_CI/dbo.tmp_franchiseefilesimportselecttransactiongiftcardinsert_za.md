# dbo.tmp_franchiseefilesimportselecttransactiongiftcardinsert_za

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselecttransactiongiftcardinsert_za"]
    dbo_tmp_franchiseefilesimportselecttransactiongiftcardinsert_za(["dbo.tmp_franchiseefilesimportselecttransactiongiftcardinsert_za"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselecttransactiongiftcardinsert_za |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselecttransactiongiftcardinsert_za] AS SELECT [FranchiseeTransactionHeaderID], [FranchiseeTransactionGiftCardID], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Units], [GiftCardAmount], [Discount], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [UpdateDate] FROM [dbo].[tmp_franchiseefilesimportselecttransactiongiftcardinsert_za]
```

