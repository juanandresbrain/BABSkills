# dbo.vwDate_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDate_Dim"]
    date_dim(["date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |

## View Code

```sql
CREATE  VIEW dbo.vwDate_Dim
AS

SELECT *
FROM date_dim
WHERE fiscal_week in (52,53)
	and fiscal_year = 2003
```

