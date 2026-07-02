# dbo.Sl_Md_FieldGrouping

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_FieldGrouping"]
    dbo_Md_FieldGrouping(["dbo.Md_FieldGrouping"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_FieldGrouping |

## View Code

```sql
create view [dbo].[Sl_Md_FieldGrouping] 
(field_group_id, field_id)
AS SELECT field_group_id, field_id
FROM fn_01.dbo.Md_FieldGrouping
```

