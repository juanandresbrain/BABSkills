# dbo.vwFiscal_Period_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwFiscal_Period_Dim"]
    date_dim(["date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |

## View Code

```sql
CREATE   VIEW dbo.vwFiscal_Period_Dim
AS

SELECT 	DISTINCT
	 fiscal_period
	,fiscal_quarter
	,fiscal_year
	,period_of_quarter
	,period_id
	,quarter_id

FROM date_dim
WHERE period_id is not null
```

