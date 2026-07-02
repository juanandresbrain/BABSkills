# dbo.view_style_employee

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_employee"]
    dbo_view_style_employee(["dbo.view_style_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_style_employee |

## View Code

```sql
CREATE  VIEW [dbo].view_style_employee
AS

SELECT * FROM me_01.dbo.view_style_employee
```

