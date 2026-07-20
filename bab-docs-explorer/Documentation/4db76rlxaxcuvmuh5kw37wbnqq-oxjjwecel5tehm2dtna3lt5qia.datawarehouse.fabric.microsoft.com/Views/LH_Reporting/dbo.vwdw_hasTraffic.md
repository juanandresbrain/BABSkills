# dbo.vwdw_hasTraffic

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_hasTraffic"]
    vwdw_shoppertrak_cube_v3(["vwdw_shoppertrak_cube_v3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwdw_shoppertrak_cube_v3 |

## View Code

```sql
CREATE VIEW vwdw_hasTraffic AS 
SELECT        
store_key, date_key, time_key, Enters, Exits
, calc, isShopperTrakHours, isSTComp
, isSTCompNextYear, isCompThisYear
, isCompNextYear, isSOTF,                           
hasTraffic 
FROM  vwdw_shoppertrak_cube_v3
```

