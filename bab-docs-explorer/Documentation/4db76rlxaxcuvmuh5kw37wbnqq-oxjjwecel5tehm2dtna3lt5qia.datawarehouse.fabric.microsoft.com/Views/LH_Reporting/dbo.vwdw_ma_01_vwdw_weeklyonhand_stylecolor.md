# dbo.vwdw_ma_01_vwdw_weeklyonhand_stylecolor

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_ma_01_vwdw_weeklyonhand_stylecolor"]
    dbo_ma_01_vwdw_weeklyonhand_stylecolor(["dbo.ma_01_vwdw_weeklyonhand_stylecolor"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ma_01_vwdw_weeklyonhand_stylecolor |

## View Code

```sql
create view dbo.vwdw_ma_01_vwdw_weeklyonhand_stylecolor
AS
select * from LH_Source.dbo.ma_01_vwdw_weeklyonhand_stylecolor
```

