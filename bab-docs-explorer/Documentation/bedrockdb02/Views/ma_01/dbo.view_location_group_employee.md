# dbo.view_location_group_employee

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_location_group_employee"]
    dbo_view_location_group_employee(["dbo.view_location_group_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_location_group_employee |

## View Code

```sql
CREATE  VIEW [dbo].view_location_group_employee
AS

SELECT * FROM me_01.dbo.view_location_group_employee
```

