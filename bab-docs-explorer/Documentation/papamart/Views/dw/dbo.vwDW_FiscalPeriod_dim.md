# dbo.vwDW_FiscalPeriod_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_FiscalPeriod_dim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW dbo.vwDW_FiscalPeriod_dim
as 
select fiscal_year, fiscal_quarter,fiscal_period
from dbo.date_dim with (nolock)
```

