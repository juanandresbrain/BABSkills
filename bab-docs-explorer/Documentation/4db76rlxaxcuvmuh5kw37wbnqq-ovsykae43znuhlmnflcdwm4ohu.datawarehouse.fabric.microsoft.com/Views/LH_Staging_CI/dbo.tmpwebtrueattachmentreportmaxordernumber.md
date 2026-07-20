# dbo.tmpwebtrueattachmentreportmaxordernumber

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmpwebtrueattachmentreportmaxordernumber"]
    dbo_tmpwebtrueattachmentreportmaxordernumber(["dbo.tmpwebtrueattachmentreportmaxordernumber"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpwebtrueattachmentreportmaxordernumber |

## View Code

```sql
; CREATE   VIEW [dbo].[tmpwebtrueattachmentreportmaxordernumber] AS SELECT [TransactionID], [MaxOrderId], [MaxOrderNum] COLLATE Latin1_General_CI_AS AS [MaxOrderNum] FROM [dbo].[tmpwebtrueattachmentreportmaxordernumber]
```

