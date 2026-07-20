# dbo.webtransactions

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webtransactions"]
    dbo_webtransactions(["dbo.webtransactions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webtransactions |

## View Code

```sql
; CREATE   VIEW [dbo].[webtransactions] AS SELECT [TransactionID], [TransactionNum] COLLATE Latin1_General_CI_AS AS [TransactionNum], [TransactionDateTime], [TaxAmount], [TaxJurisdiction] COLLATE Latin1_General_CI_AS AS [TaxJurisdiction] FROM [dbo].[webtransactions]
```

