# dbo.franchiseetransactionorphans

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionorphans"]
    dbo_franchiseetransactionorphans(["dbo.franchiseetransactionorphans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionorphans |

## View Code

```sql
;
CREATE   VIEW [dbo].[franchiseetransactionorphans]
AS
    SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [HeaderRecords] COLLATE Latin1_General_CI_AS AS [HeaderRecords], [PaymentRecords] COLLATE Latin1_General_CI_AS AS [PaymentRecords], [MerchandiseRecords] COLLATE Latin1_General_CI_AS AS [MerchandiseRecords], [GiftCardRecords] COLLATE Latin1_General_CI_AS AS [GiftCardRecords], [OrphanMessage] COLLATE Latin1_General_CI_AS AS [OrphanMessage], [EmptyColumnsFound] COLLATE Latin1_General_CI_AS AS [EmptyColumnsFound]
    FROM LH_Staging.[dbo].[franchiseetransactionorphans]
```

