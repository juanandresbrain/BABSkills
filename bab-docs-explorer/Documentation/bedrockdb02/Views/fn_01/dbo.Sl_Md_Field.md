# dbo.Sl_Md_Field

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Field"]
    dbo_Md_Field(["dbo.Md_Field"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Field |

## View Code

```sql
create view [dbo].[Sl_Md_Field] 
(field_id, 
field_owner_id, 
table_id, 
topic_id, 
field_label_1, 
field_label_2, 
field_description_1, 
field_description_2, 
field_expression_1, 
field_expression_2, 
field_type, 
field_format, 
field_width, 
field_size, 
field_permission, 
input_mask, 
field_flags, 
default_method, 
lookup_type, 
lookup_id, 
short_label_1, 
short_label_2, 
field_period_group_id, 
subfield_lookup_id, 
native_type_syb, 
native_type_ora, 
native_type_sql, 
resource_id_1, 
resource_id_2,
field_min_value,
field_max_value)
AS SELECT field_id, 
field_owner_id, 
table_id, 
topic_id, 
field_label_1, 
field_label_2, 
field_description_1, 
field_description_2, 
field_expression_1, 
field_expression_2, 
field_type, 
field_format, 
field_width, 
field_size, 
field_permission, 
input_mask, 
field_flags, 
default_method, 
lookup_type, 
lookup_id, 
short_label_1, 
short_label_2, 
field_period_group_id, 
subfield_lookup_id, 
native_type_syb, 
native_type_ora, 
native_type_sql, 
resource_id_1, 
resource_id_2,
field_min_value,
field_max_value
FROM fn_01.dbo.Md_Field
```

