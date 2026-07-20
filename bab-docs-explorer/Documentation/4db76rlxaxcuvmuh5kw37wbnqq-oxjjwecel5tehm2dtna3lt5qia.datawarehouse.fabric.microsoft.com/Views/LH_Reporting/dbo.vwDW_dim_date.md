# dbo.vwDW_dim_date

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
CREATE   VIEW dbo.vwDW_dim_date
AS
SELECT *,
    fiscal_year * 100 + fiscal_week AS fiscal_week_seq
FROM LH_Mart.dbo.date_dim
WHERE date_key > 0
```

