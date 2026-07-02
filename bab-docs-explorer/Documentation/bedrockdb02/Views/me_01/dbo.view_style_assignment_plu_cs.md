# dbo.view_style_assignment_plu_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_assignment_plu_cs"]
    dbo_style_assignment_plu(["dbo.style_assignment_plu"]) --> VIEW
    dbo_style_assignment_plu_cs(["dbo.style_assignment_plu_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_assignment_plu |
| dbo.style_assignment_plu_cs |

## View Code

```sql
create view dbo.view_style_assignment_plu_cs 
AS
SELECT [style_assignment_plu_id]
      ,[style_id]
      ,[parameter_group_plu_id]
      ,[attribute_set_id]
      ,[location_id]
      ,[group_permutation_plu_id]
      ,[style_size_id]
  FROM [style_assignment_plu]
UNION ALL
SELECT [style_assignment_plu_id]
      ,[style_id]
      ,[parameter_group_plu_id]
      ,[attribute_set_id]
      ,[location_id]
      ,[group_permutation_plu_id]
      ,[style_size_id]
  FROM [style_assignment_plu_cs]
```

