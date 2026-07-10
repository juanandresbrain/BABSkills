# dbo.vwDW_FiscalQuarter_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_FiscalQuarter_dim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW dbo.vwDW_FiscalQuarter_dim
as 
select fiscal_year, fiscal_quarter
from dbo.date_dim with (nolock)
group by fiscal_quarter,fiscal_year
```

