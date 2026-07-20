# dbo.vwdw_store_shoppertrak

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_store_shoppertrak"]
    dbo_shpr_trk_trfc_fct(["dbo.shpr_trk_trfc_fct"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.shpr_trk_trfc_fct |

## View Code

```sql
-- =============================================================================================================  
 -- Name: dbo.vwDW_Store_ShopperTrak  
 --  
 -- Description: Identifies the stores which have Shopper Trak  
 --  
 -- Dependencies:   
 --  
 -- Revision History  
 --  Name:   Date:   Comments:  
 --  G Murrish  5/7/2012  Initial Release  
 -- =============================================================================================================  
 CREATE VIEW vwdw_store_shoppertrak
 AS 
 SELECT DISTINCT TOP 1 STR_KEY AS store_key  
 FROM  
 LH_Mart.dbo.shpr_trk_trfc_fct AS STTF
```

