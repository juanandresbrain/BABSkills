# dbo.tmpgrpredemptions

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpgrpredemptions"]
    dbo_tmpgrpredemptions(["dbo.tmpgrpredemptions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpgrpredemptions |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpgrpredemptions] AS SELECT [account_number] COLLATE Latin1_General_CI_AS AS [account_number], [date_key], [store_key], [terminal_id], [terminal_transaction_number], [lineID], [postedPhase], [transaction_amount], [grRecID] FROM [dbo].[tmpgrpredemptions]
```

