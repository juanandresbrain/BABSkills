# dbo.tmpwebtrueattachmentreportparentitem

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpwebtrueattachmentreportparentitem"]
    dbo_tmpwebtrueattachmentreportparentitem(["dbo.tmpwebtrueattachmentreportparentitem"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpwebtrueattachmentreportparentitem |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpwebtrueattachmentreportparentitem] AS SELECT [sku] COLLATE Latin1_General_CI_AS AS [sku], [QTY], [ItemDescription] COLLATE Latin1_General_CI_AS AS [ItemDescription], [Price], [ParentItem], [OrderNum] COLLATE Latin1_General_CI_AS AS [OrderNum], [OrderDate], [OrderItemID], [isParent], [linkID], [TransactionID] FROM [dbo].[tmpwebtrueattachmentreportparentitem]
```

