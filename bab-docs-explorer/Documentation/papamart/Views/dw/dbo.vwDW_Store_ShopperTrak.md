# dbo.vwDW_Store_ShopperTrak

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Store_ShopperTrak"]
    SHPR_TRK_TRFC_FCT(["SHPR_TRK_TRFC_FCT"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SHPR_TRK_TRFC_FCT |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Store_ShopperTrak]
-- =============================================================================================================
-- Name: [dbo].[vwDW_Store_ShopperTrak]
--
-- Description: Identifies the stores which have Shopper Trak
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		G Murrish		5/7/2012		Initial Release
-- =============================================================================================================
AS SELECT DISTINCT STR_KEY AS store_key
   FROM
	   SHPR_TRK_TRFC_FCT STTF WITH (NOLOCK)
```

