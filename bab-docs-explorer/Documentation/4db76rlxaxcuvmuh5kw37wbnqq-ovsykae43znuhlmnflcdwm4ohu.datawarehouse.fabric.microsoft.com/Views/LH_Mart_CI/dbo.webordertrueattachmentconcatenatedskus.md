# dbo.webordertrueattachmentconcatenatedskus

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webordertrueattachmentconcatenatedskus"]
    dbo_webordertrueattachmentconcatenatedskus(["dbo.webordertrueattachmentconcatenatedskus"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webordertrueattachmentconcatenatedskus |

## View Code

```sql
; CREATE   VIEW [dbo].[webordertrueattachmentconcatenatedskus] AS     SELECT [OrderNum] COLLATE Latin1_General_CI_AS AS [OrderNum], [OrderDate], [SkuString] COLLATE Latin1_General_CI_AS AS [SkuString], [DescriptionString] COLLATE Latin1_General_CI_AS AS [DescriptionString], [Quantity], [Price], [KeyStoryString] COLLATE Latin1_General_CI_AS AS [KeyStoryString], [MstatString] COLLATE Latin1_General_CI_AS AS [MstatString], [Country] COLLATE Latin1_General_CI_AS AS [Country], [InsertDate], [UpdateDate]     FROM [dbo].[webordertrueattachmentconcatenatedskus]
```

