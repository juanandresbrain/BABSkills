# dbo.franchiseetransactiongiftcardimport

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactiongiftcardimport"]
    dbo_franchiseetransactiongiftcardimport(["dbo.franchiseetransactiongiftcardimport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactiongiftcardimport |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseetransactiongiftcardimport]
AS
    SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Units], [GiftCardAmount], [Discount], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee]
    FROM LH_Staging.[dbo].[franchiseetransactiongiftcardimport]
```

