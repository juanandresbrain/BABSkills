# dbo.vwDW_dim_date

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_date"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_date]
AS

	SELECT *
	FROM dbo.date_dim
	WHERE date_key > 0
```

