# dbo.vwdw_destination_currency

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_destination_currency"]
    vwdw_currency_dim(["vwdw_currency_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwdw_currency_dim |

## View Code

```sql
CREATE VIEW vwdw_destination_currency
AS
SELECT * FROM vwdw_currency_dim
```

