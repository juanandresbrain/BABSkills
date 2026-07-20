# dbo.utahourtype

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utahourtype"]
    dbo_utahourtype(["dbo.utahourtype"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utahourtype |

## View Code

```sql
; CREATE   VIEW [dbo].[utahourtype] AS     SELECT [Htype_ID], [Htype_Name] COLLATE Latin1_General_CI_AS AS [Htype_Name], [InsertDate], [UpdateDate]     FROM [dbo].[utahourtype]
```

