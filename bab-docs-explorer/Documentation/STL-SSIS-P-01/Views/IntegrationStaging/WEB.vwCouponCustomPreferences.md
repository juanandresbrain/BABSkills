# WEB.vwCouponCustomPreferences

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwCouponCustomPreferences"]
    WEB_DiscountCouponExport(["WEB.DiscountCouponExport"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.DiscountCouponExport |

## View Code

```sql
CREATE view [WEB].[vwCouponCustomPreferences]

as 

--------------------------------------------------------------------------------------------------
-- vwLocations - Outputs XML of custom preferences for coupons export for eCommerce
--- 2018-03-16 - Tim Bytnar - Created View
--------------------------------------------------------------------------------------------------

SELECT '<?xml version="1.0" encoding="UTF-8"?>
		<preferences xmlns="http://www.demandware.com/xml/impex/preferences/2007-03-31"><custom-preferences><staging>' + 
		CAST((
				select 
					'crmLoyaltyRewardCouponIDs' as '@preference-id',
					(SELECT					
						couponNumber as value
						from [WEB].[DiscountCouponExport]
						FOR XML PATH (''), TYPE)
				FOR XML PATH ('preference')
) as varchar(max)) +
'</staging></custom-preferences></preferences>' as XMLOutput
```

