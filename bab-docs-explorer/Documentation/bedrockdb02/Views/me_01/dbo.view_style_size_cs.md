# dbo.view_style_size_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_size_cs"]
    dbo_style_size(["dbo.style_size"]) --> VIEW
    dbo_style_size_cs(["dbo.style_size_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_size |
| dbo.style_size_cs |

## View Code

```sql
create view dbo.view_style_size_cs 
AS
SELECT [style_size_id]
      ,[style_id]
      ,[size_master_id]
      ,[reorder_flag]
      ,[ticket_label_override]
  FROM [style_size]
UNION ALL
SELECT [style_size_id]
      ,[style_id]
      ,[size_master_id]
      ,[reorder_flag]
      ,[ticket_label_override]
  FROM [style_size_cs]
```

