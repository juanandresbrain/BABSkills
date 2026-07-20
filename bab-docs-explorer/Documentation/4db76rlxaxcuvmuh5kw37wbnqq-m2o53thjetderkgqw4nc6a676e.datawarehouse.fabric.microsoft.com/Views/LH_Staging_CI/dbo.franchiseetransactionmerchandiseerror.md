# dbo.franchiseetransactionmerchandiseerror

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionmerchandiseerror"]
    dbo_franchiseetransactionmerchandiseerror(["dbo.franchiseetransactionmerchandiseerror"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionmerchandiseerror |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseetransactionmerchandiseerror]
AS
    SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Style] COLLATE Latin1_General_CI_AS AS [Style], [Units] COLLATE Latin1_General_CI_AS AS [Units], [Cost] COLLATE Latin1_General_CI_AS AS [Cost], [GrossSales] COLLATE Latin1_General_CI_AS AS [GrossSales], [Discount] COLLATE Latin1_General_CI_AS AS [Discount], [VAT] COLLATE Latin1_General_CI_AS AS [VAT], [InsertDate] COLLATE Latin1_General_CI_AS AS [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc], [ErrorSource] COLLATE Latin1_General_CI_AS AS [ErrorSource]
    FROM LH_Staging.[dbo].[franchiseetransactionmerchandiseerror]
```

