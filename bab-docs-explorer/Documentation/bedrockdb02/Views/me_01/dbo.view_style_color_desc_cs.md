# dbo.view_style_color_desc_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_color_desc_cs"]
    dbo_style_color_desc_cs(["dbo.style_color_desc_cs"]) --> VIEW
    dbo_style_color_description(["dbo.style_color_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_color_desc_cs |
| dbo.style_color_description |

## View Code

```sql
create view dbo.view_style_color_desc_cs 
AS
SELECT [style_color_description_id]
      ,[style_color_id]
      ,[language_id]
      ,[long_desc]
      ,[short_desc]
  FROM [style_color_description]
UNION ALL
SELECT [style_color_description_id]
      ,[style_color_id]
      ,[language_id]
      ,[long_desc]
      ,[short_desc]
  FROM [style_color_desc_cs]
```

