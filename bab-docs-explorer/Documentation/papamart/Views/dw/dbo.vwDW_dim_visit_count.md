# dbo.vwDW_dim_visit_count

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_visit_count"]
    dbo_dim_customer_visit_count(["dbo.dim_customer_visit_count"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dim_customer_visit_count |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_visit_count]
AS

	SELECT *
  FROM [dw].[dbo].[dim_customer_visit_count]
```

