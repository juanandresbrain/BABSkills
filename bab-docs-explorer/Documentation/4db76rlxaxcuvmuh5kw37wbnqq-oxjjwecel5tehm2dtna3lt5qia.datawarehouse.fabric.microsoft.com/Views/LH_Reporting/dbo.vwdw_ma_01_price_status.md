# dbo.vwdw_ma_01_price_status

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_ma_01_price_status"]
    dbo_ma_01_price_status(["dbo.ma_01_price_status"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ma_01_price_status |

## View Code

```sql
create view dbo.vwdw_ma_01_price_status
AS
select * from LH_Source.dbo.ma_01_price_status
```

