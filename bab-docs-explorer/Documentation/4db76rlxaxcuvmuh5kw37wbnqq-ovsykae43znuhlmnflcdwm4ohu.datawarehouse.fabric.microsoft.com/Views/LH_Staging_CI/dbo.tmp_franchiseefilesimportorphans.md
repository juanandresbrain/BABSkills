# dbo.tmp_franchiseefilesimportorphans

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportorphans"]
    dbo_tmp_franchiseefilesimportorphans(["dbo.tmp_franchiseefilesimportorphans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportorphans |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportorphans] AS SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [HeaderRecords] COLLATE Latin1_General_CI_AS AS [HeaderRecords], [PaymentRecords] COLLATE Latin1_General_CI_AS AS [PaymentRecords], [MerchandiseRecords] COLLATE Latin1_General_CI_AS AS [MerchandiseRecords], [GiftCardRecords] COLLATE Latin1_General_CI_AS AS [GiftCardRecords], [OrphanMessage] COLLATE Latin1_General_CI_AS AS [OrphanMessage] FROM [dbo].[tmp_franchiseefilesimportorphans]
```

