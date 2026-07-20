# dbo.franchiseetransactionheaderdiscountsimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionheaderdiscountsimport"]
    dbo_franchiseetransactionheaderdiscountsimport(["dbo.franchiseetransactionheaderdiscountsimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionheaderdiscountsimport |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseetransactionheaderdiscountsimport]
AS
    SELECT [HeaderDiscount], [TRANSACTIONID] COLLATE Latin1_General_CI_AS AS [TRANSACTIONID]
    FROM LH_Staging.[dbo].[franchiseetransactionheaderdiscountsimport]
```

