# dbo.vwDW_date_dim_FirstDateOfFiscalMonth

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_date_dim_FirstDateOfFiscalMonth"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_date_dim_FirstDateOfFiscalMonth]
AS
	SELECT CAST(MIN(actual_date) as date) as Date
	from papamart.dw.dbo.date_dim
	GROUP BY fiscal_period,fiscal_year
```

