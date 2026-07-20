# dbo.tmp_franchiseefilesimportselecttransactionheaderinsert_cn

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimportselecttransactionheaderinsert_cn"]
    dbo_tmp_franchiseefilesimportselecttransactionheaderinsert_cn(["dbo.tmp_franchiseefilesimportselecttransactionheaderinsert_cn"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimportselecttransactionheaderinsert_cn |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimportselecttransactionheaderinsert_cn] AS SELECT [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [TransactionDateTime], [StoreID] COLLATE Latin1_General_CI_AS AS [StoreID], [RawStoreID] COLLATE Latin1_General_CI_AS AS [RawStoreID], [InsertDate], [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [store_key], [date_key], [time_key], [UpdateDate] FROM [dbo].[tmp_franchiseefilesimportselecttransactionheaderinsert_cn]
```

