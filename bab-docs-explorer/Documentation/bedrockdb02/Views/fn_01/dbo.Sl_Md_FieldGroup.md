# dbo.Sl_Md_FieldGroup

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_FieldGroup"]
    dbo_Md_FieldGroup(["dbo.Md_FieldGroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_FieldGroup |

## View Code

```sql
create view [dbo].[Sl_Md_FieldGroup] 
(topic_id, field_group_id, field_group_label_1, field_group_label_2, field_group_description_1, field_group_description_2, parent_field_group_id, display_fields, resource_id)
AS SELECT topic_id, field_group_id, field_group_label_1, field_group_label_2, field_group_description_1, field_group_description_2, parent_field_group_id, display_fields, resource_id
FROM fn_01.dbo.Md_FieldGroup
```

