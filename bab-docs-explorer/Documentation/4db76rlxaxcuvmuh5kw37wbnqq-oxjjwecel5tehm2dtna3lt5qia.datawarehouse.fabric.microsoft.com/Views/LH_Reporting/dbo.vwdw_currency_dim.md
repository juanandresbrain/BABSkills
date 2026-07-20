# dbo.vwdw_currency_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_currency_dim"]
    dbo_currency_dim(["dbo.currency_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.currency_dim |

## View Code

```sql
CREATE VIEW vwdw_currency_dim
AS 
SELECT * FROM LH_Mart.dbo.currency_dim
```

