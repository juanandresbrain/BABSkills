# dbo.line_object_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.line_object_dim"]
    dbo_line_object_dim(["dbo.line_object_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.line_object_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[line_object_dim] AS     SELECT [Line_Object_Key], [Line_Object], [Line_Object_Type], [Line_Object_Description] COLLATE Latin1_General_CI_AS AS [Line_Object_Description], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID]     FROM LH_Mart.[dbo].[line_object_dim]
```

