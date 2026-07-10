# dbo.vwDW_FiscalYear_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_FiscalYear_dim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW vwDW_FiscalYear_dim
as 
select fiscal_year 
from dbo.date_dim with (nolock)
group by fiscal_year
```

