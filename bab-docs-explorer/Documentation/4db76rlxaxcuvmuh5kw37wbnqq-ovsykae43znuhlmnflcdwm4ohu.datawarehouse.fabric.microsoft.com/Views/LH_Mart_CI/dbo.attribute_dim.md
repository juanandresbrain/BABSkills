# dbo.attribute_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.attribute_dim"]
    dbo_attribute_dim(["dbo.attribute_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[attribute_dim] AS     SELECT [entity_key] COLLATE Latin1_General_CI_AS AS [entity_key], [style_code], [AttributeName] COLLATE Latin1_General_CI_AS AS [AttributeName], [AttributeValue] COLLATE Latin1_General_CI_AS AS [AttributeValue], [INS_DT], [UPDT_DT]     FROM [dbo].[attribute_dim]
```

