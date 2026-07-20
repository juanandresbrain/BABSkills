# dbo.tmp_franchiseefilesimportdupes

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportdupes"]
    dbo_tmp_franchiseefilesimportdupes(["dbo.tmp_franchiseefilesimportdupes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportdupes |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportdupes] AS SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [HeaderRecords], [PaymentRecords], [MerchandiseRecords], [GiftCardRecords] FROM [dbo].[tmp_franchiseefilesimportdupes]
```

