# dbo.franchiseetransactionheaderimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionheaderimport"]
    dbo_franchiseetransactionheaderimport(["dbo.franchiseetransactionheaderimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionheaderimport |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseetransactionheaderimport]
AS
    SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDateTime], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee]
    FROM LH_Staging.[dbo].[franchiseetransactionheaderimport]
```

