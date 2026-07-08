# dbo.Lg_Md_FieldGroup

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Lg_Md_FieldGroup"]
    Lg_DependentDesc(["Lg_DependentDesc"]) --> VIEW
    Md_FieldGroup(["Md_FieldGroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Lg_DependentDesc |
| Md_FieldGroup |

## View Code

```sql
create view dbo.Lg_Md_FieldGroup  AS
	SELECT a.topic_id, a.field_group_id, a.field_group_label_1, a.field_group_label_2, ISNULL(b.first_pair_text, a.field_group_label_1) as field_group_label_3,
	       a.field_group_description_1, a.field_group_description_2, ISNULL(b.second_pair_text, a.field_group_description_1) as field_group_description_3,
	       a.parent_field_group_id, a.display_fields, a.resource_id, 
               a.field_group_lbl_resource_name,
               b.language_id
	  FROM Md_FieldGroup a LEFT OUTER JOIN Lg_DependentDesc b ON a.resource_id = b.resource_id
```

