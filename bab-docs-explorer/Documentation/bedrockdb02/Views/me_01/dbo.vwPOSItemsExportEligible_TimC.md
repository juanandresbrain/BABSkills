# dbo.vwPOSItemsExportEligible_TimC

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSItemsExportEligible_TimC"]
    dbo_attribute(["dbo.attribute"]) --> VIEW
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_POSProductCatalogMasterAttributes(["dbo.POSProductCatalogMasterAttributes"]) --> VIEW
    dbo_POSProductHardLaunchItems(["dbo.POSProductHardLaunchItems"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_vwPOSItemsAllocated(["dbo.vwPOSItemsAllocated"]) --> VIEW
    dbo_vwPOSItemsOnHand(["dbo.vwPOSItemsOnHand"]) --> VIEW
    dbo_vwPOSOutbound_PromotionItemGroupsDistinct(["dbo.vwPOSOutbound_PromotionItemGroupsDistinct"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.POSProductCatalogMasterAttributes |
| dbo.POSProductHardLaunchItems |
| dbo.style |
| dbo.vwPOSItemsAllocated |
| dbo.vwPOSItemsOnHand |
| dbo.vwPOSOutbound_PromotionItemGroupsDistinct |

## View Code

```sql
CREATE view [dbo].[vwPOSItemsExportEligible_TimC]

--------------------------------------------------------------------------------------------------------------------------------------
--Tim Callahan	 2023-05-01 -- Created view for Jumpmind POS Product Dataset for Eligibility to Export Reference as related to JIRA BIB544
--Tim Callahan	 2023-05-15 -- Modified view added some additional conditions to allow some Donation, Gift Card and Service Items to Be included which likely will not have inventory
--Tim Callahan	 2023-06-15 -- Modified Handling for Some Items that must be stock item type but dont have inventory 
--Dan Tweedie	 2023-06-23	-- Changed MerchInDate buffer from 7 days to 10 (rolled back until Amy S finally confirms)
--Tim Callahan	 2023-07-07 -- Modified Handling for additional items that must be stock item type but dont have inventory see JIRA BIB-599 for details 
--Dan Tweedie    2023-07-26	-- Added allowance for items that are in an item group for an Aptos deal -- there might be very low inventory items that we might not have on hand but supposedly is available in stores in very small qty
--Tim Callahan	 2023-09-27 -- Modified the 7/26/2023 filter condition to still exclude Hard Launch and Future IDate Styles	
--							   Also had to change the item group filter to a left join due to very peformance of in clause 
--Tim Callahan	 2023-10-18	-- Additional Handling for UK\IE for time difference we will send the UK\IE skus 1 additional day early for all date IDATE driven conditions 
--------------------------------------------------------------------------------------------------------------------------------------

as


with InfInv as
(
select 
s.style_code as StyleCode,
ats.attribute_set_label as InventoryLabel
from bedrockdb02.me_01.dbo.attribute a (nolock)
join bedrockdb02.me_01.dbo.entity_attribute_set eas  (nolock) on a.attribute_id = eas.attribute_id 
join bedrockdb02.me_01.dbo.attribute_set ats  (nolock)
    on a.attribute_id = ats.attribute_id 
    and eas.attribute_set_id = ats.attribute_set_id 
    and ats.active_flag = 1
join bedrockdb02.me_01.dbo.style s on eas.parent_id = s.style_id 
where 1=1
and s.active_flag = 1 -- Active Styles Only
and a.attribute_code = 'WEBINV' 
and ats.attribute_set_label = 'INFINITE INVENTORY'
) 


select 
datediff(dd,p.MerchInDate,getdate()) as DateDifference,
p.Style_Code, 
p.SKUDescription, 
p.UPC, 
p.ProductSellingGeography, 
p.MerchInDate, 
--p.merchOutDate, 
hl.StyleCode as HardLaunchStyleCode, 
ia.QuantityAllocated, 
ioh.TotalUnitsAvailable, 
P.ItemType, 
ig.style_code as PromoItemGroupStyle
--,p.* 
from POSProductCatalogMasterAttributes p 
left join POSProductHardLaunchItems hl on p.Style_Code=hl.StyleCode and hl.CountryCode=p.ProductSellingGeography -- Created this table as related to JIRA BIB544
left join vwPOSItemsAllocated ia on ia.style_code=p.Style_Code and ia.ProductSellingGeography=p.ProductSellingGeography -- Created this view as related to JIRA BIB544
left join vwPOSItemsOnHand ioh on ioh.style_code = p.Style_Code and ioh.ProductSellingGeography=p.ProductSellingGeography -- Created this view as related to JIRA BIB544
left join InfInv i on i.StyleCode=p.Style_Code
left join vwPOSOutbound_PromotionItemGroupsDistinct ig on ig.style_code=p.Style_Code 
where 1=1
and  
(
		(
			DATEDIFF(dd,p.MerchInDate, getdate()) >= -7
			and 
			p.ItemType = 'STOCK'
			and 
			(
			ia.style_code is not null -- Allocated Inventory in Chain
				or 
			ioh.style_code is not null  -- On Hand Inventory in Chain								  
				or 
			p.Department in ('Canadian Fees','Misc.Fees','Party Fees','Transaction Flags','UK Fees','UK UK Mandated Fees','UK-Misc. Fees','UK-Transaction Flags','US State Mandated Fees') -- Added 6/15/2023 
				or
			left(p.HierarchyGroupCode,8) in ('R-B-D-46','R-B-U-46', 'R-B-D-65') -- Donations\Embroidery -- Added 7/7/2023
				or
			p.HierarchyGroupCode in ('W-C-K-12-01-07','W-D-K-12-01-07','W-E-K-12-01-07','W-F-K-12-01-07','R-B-D-80-02-00','R-B-U-80-02-00') --Digital Blanks\Virtual GiftCards -- Added 7/7/2023
				or
			i.StyleCode is not null -- Infinite Inventory Item -- Added 7/7/2023
			)			
			-- This is excluding older styles that do not have any inventory existing or allocated in the Item Country 

		) -- IDATE Is Today or In the Past 
	or
	(
			DATEDIFF(dd,p.MerchInDate, getdate()) >= 0 
			and 
			p.ItemType <> 'STOCK'
	)	--  IDATE Is Today or In the Past , not a stock a item type and doesn't check for inventory nor allocations -- Added 5/15/2023
	or 
		(
		 hl.StyleCode is not null 
			and 
			--DATEDIFF(dd,p.MerchInDate, getdate()) >= -1 -- Replaced With Below on  10/18/2023
			(
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -1 and p.ProductSellingGeography in ('US','CA')) 
					or 
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -2 and p.ProductSellingGeography in ('UK','IE')) 
			)
		) -- Hard Launch Item and 1 Prior to IDATE being active 
	or 
		(
			hl.StyleCode is null 
				and 
			--DATEDIFF(dd,p.MerchInDate, getdate()) >= -7 -- Replaced With Below on  10/18/2023
			(
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -7 and p.ProductSellingGeography in ('US','CA')) 
					or 
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -8 and p.ProductSellingGeography in ('UK','IE')) 
			)
				and 
					(
					isnull(ia.QuantityAllocated,0) > 0 
						or 
					isnull(ioh.TotalUnitsAvailable,0) > 0 
					)
		) -- Not a Hard Launch Item but the IDATE is 7 Days  or less in the future and there is inventory or allocation in the country\ProductSellingGeography


	OR
		(		
			--p.Style_Code in (select style_code from vwPOSOutbound_PromotionItemGroups)
			ig.style_code is not null 
				and 
			hl.StyleCode is not null 
				and 
			--DATEDIFF(dd,p.MerchInDate, getdate()) >= -1 -- Replaced 10/18/2023
			(
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -1 and p.ProductSellingGeography in ('US','CA')) 
					or 
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -2 and p.ProductSellingGeography in ('UK','IE')) 
			)
			
		 ) -- In POS Promotion Item group and is a Hard Launch Item and 1 Prior to IDATE being active 
	
	OR  
		(
			--p.Style_Code in (select style_code from vwPOSOutbound_PromotionItemGroups)
			ig.style_code is not null 
				and
			hl.StyleCode is null 
				and 
			--DATEDIFF(dd,p.MerchInDate, getdate()) >= -7 -- Replaced With Below on  10/18/2023
			(
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -7 and p.ProductSellingGeography in ('US','CA')) 
					or 
				(DATEDIFF(dd,p.MerchInDate, getdate()) >= -8 and p.ProductSellingGeography in ('UK','IE')) 
			)
		) -- In POS Promotion Item Group and is NOT a Hard Launch Item and 7 Prior to IDATE being active 

	OR p.style_code in --forced exception list
		(
			'032579',
			'031745',
			'031742',
			'031756',
			'031744',
			'031746',
			'032642',
			'032733',
			'032729',
			'033559',
			'033584',
			'033585',
			'033586'
		)
) 
AND p.style_code not in ---LIST OF FEES AND GWP'S FROM KASEY THAT SHOULD NOT BE INCLUDED - HARD CODING FOR NOW
	(
		'000014',
		'000015',
		'000016',
		'000017',
		'000024',
		'000025',
		'000026',
		'000027',
		'000028',
		'000029',
		'000032',
		'000035',
		'000038',
		'000042',
		'000044',
		'000078',
		'000077',
		'000079',
		'000081',
		'000082',
		'023019',
		'056065',
		'098045',
		'098046',
		'098047',
		'400003'
	)
AND right(p.style_code,5) not in 
	(
		--'80083',  Kasey Palmer 6/12/24  "I'm ok if we want to just reactive or unarchive the one sku for Service party"
		'80009',
		'80056',
		'80014',
		'80019',
		'80036',
		'80061',
		'80068',
		'80094',
		'80115',
		'89501',
		'89502',
		'89503',
		'90674',
		'89504',
		'90717',
		'90814',
		'90817',
		'90817',
		'91329',
		'91769',
		'91896',
		'55391',
		'57860',
		'80003',
		'80057',
		'80058',
		'80059',
		'80069',
		'80082',
		'80084',
		'80139',
		'90807',
		'91032',
		'91033',
		'91160',
		'80139'
	)
```

