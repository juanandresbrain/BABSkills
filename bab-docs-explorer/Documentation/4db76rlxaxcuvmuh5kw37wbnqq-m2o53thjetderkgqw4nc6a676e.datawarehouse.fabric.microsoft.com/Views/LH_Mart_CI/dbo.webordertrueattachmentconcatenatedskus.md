# dbo.webordertrueattachmentconcatenatedskus

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
;

CREATE VIEW dbo.webordertrueattachmentconcatenatedskus AS SELECT OrderNum COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OrderNum, OrderDate, SkuString COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SkuString, DescriptionString COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS DescriptionString, Quantity, Price, KeyStoryString COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS KeyStoryString, MstatString COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MstatString, Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Country, InsertDate, UpdateDate FROM LH_Mart.dbo.webordertrueattachmentconcatenatedskus;;
```

