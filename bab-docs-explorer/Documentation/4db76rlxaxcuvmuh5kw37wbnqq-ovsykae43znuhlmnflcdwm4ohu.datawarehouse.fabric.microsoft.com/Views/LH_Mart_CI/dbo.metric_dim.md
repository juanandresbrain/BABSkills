# dbo.metric_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.metric_dim"]
    dbo_metric_dim(["dbo.metric_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.metric_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[metric_dim] AS     SELECT [metric_dim_key], [name] COLLATE Latin1_General_CI_AS AS [name], [description] COLLATE Latin1_General_CI_AS AS [description], [source] COLLATE Latin1_General_CI_AS AS [source]     FROM [dbo].[metric_dim]
```

