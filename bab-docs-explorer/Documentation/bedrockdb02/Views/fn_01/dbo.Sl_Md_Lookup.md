# dbo.Sl_Md_Lookup

**Database:** fn_01  
**Server:** bedrockdb02  

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
create view [dbo].[Sl_Md_Lookup] (
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
FROM fn_01.dbo.Md_Lookup
```

