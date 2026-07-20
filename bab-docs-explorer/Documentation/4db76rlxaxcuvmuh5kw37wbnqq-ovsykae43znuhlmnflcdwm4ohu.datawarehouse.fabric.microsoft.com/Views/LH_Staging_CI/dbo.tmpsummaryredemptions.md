# dbo.tmpsummaryredemptions

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpsummaryredemptions"]
    dbo_tmpsummaryredemptions(["dbo.tmpsummaryredemptions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpsummaryredemptions |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpsummaryredemptions] AS SELECT [account_number] COLLATE Latin1_General_CI_AS AS [account_number], [store_key], [date_key], [terminal_id], [terminal_transaction_number], [transaction_amount], [LineID], [gaRecID], [postedPhase] FROM [dbo].[tmpsummaryredemptions]
```

