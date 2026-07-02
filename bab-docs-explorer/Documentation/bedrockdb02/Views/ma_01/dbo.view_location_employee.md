# dbo.view_location_employee

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_location_employee"]
    dbo_view_location_employee(["dbo.view_location_employee"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_location_employee |

## View Code

```sql
CREATE  VIEW [dbo].view_location_employee
AS

SELECT * FROM me_01.dbo.view_location_employee
```

