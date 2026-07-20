# dbo.vwdw_inventory_status

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_inventory_status"]
    dbo_ma_01_vwdw_dim_inventorystatus(["dbo.ma_01_vwdw_dim_inventorystatus"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ma_01_vwdw_dim_inventorystatus |

## View Code

```sql
create view vwdw_inventory_status
   as
   select * from [LH_Source].[dbo].[ma_01_vwdw_dim_inventorystatus]
```

