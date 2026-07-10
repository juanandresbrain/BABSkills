# dbo.vwDW_dim_customer_demographics

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_customer_demographics"]
    dbo_dim_customer_demographics(["dbo.dim_customer_demographics"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dim_customer_demographics |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_customer_demographics]
AS

	SELECT *
	FROM dbo.dim_customer_demographics
```

