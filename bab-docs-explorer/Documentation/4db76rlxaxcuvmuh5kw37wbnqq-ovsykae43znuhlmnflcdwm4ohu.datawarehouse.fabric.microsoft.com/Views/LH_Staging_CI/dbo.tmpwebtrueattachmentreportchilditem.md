# dbo.tmpwebtrueattachmentreportchilditem

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpwebtrueattachmentreportchilditem"]
    dbo_tmpwebtrueattachmentreportchilditem(["dbo.tmpwebtrueattachmentreportchilditem"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpwebtrueattachmentreportchilditem |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpwebtrueattachmentreportchilditem] AS SELECT [sku] COLLATE Latin1_General_CI_AS AS [sku], [QTY], [ItemDescription] COLLATE Latin1_General_CI_AS AS [ItemDescription], [Price], [ParentItem], [OrderNum] COLLATE Latin1_General_CI_AS AS [OrderNum], [OrderDate], [OrderItemID], [isParent], [linkID], [TransactionID] FROM [dbo].[tmpwebtrueattachmentreportchilditem]
```

