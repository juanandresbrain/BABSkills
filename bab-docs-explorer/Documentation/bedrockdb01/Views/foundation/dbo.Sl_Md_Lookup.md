# dbo.Sl_Md_Lookup

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Lookup"]
    dbo_Md_Lookup(["dbo.Md_Lookup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Lookup |

## View Code

```sql
create view dbo.Sl_Md_Lookup (
lookup_id, 
lookup_descritpion_1, 
lookup_descritpion_2, 
table_id, 
display_expression_1, 
display_expression_2, 
value_expression, 
resolve_join, 
where_expression
)
AS SELECT 
lookup_id, 
lookup_descritpion_1, 
lookup_descritpion_2, 
table_id, 
display_expression_1, 
display_expression_2, 
value_expression, 
resolve_join, 
where_expression
FROM foundation.dbo.Md_Lookup
```

