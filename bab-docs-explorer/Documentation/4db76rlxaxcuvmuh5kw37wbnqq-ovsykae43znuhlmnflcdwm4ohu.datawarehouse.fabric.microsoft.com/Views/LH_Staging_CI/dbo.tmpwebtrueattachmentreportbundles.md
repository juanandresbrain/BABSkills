# dbo.tmpwebtrueattachmentreportbundles

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpwebtrueattachmentreportbundles"]
    dbo_tmpwebtrueattachmentreportbundles(["dbo.tmpwebtrueattachmentreportbundles"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpwebtrueattachmentreportbundles |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpwebtrueattachmentreportbundles] AS SELECT [sku] COLLATE Latin1_General_CI_AS AS [sku], [QTY], [ItemDescription] COLLATE Latin1_General_CI_AS AS [ItemDescription], [Price], [ParentItem], [OrderNum] COLLATE Latin1_General_CI_AS AS [OrderNum], [OrderDate], [OrderItemID], [isParent], [linkID], [TransactionID] FROM [dbo].[tmpwebtrueattachmentreportbundles]
```

