# NOCDev.spGetWeeklyUpdateSets

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["NOCDev.spGetWeeklyUpdateSets"]
    dbo_UpdateLog(["dbo.UpdateLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UpdateLog |

## Stored Procedure Code

```sql
CREATE proc [NOCDev].[spGetWeeklyUpdateSets]

as

-------------------------------------------------------------------------					
-- 2021-11-16 - Brandon Hickey - Created Proc
-------------------------------------------------------------------------

set nocount on

DECLARE @start_of_week AS DateTime;
SET @start_of_week = dateadd(week, datediff(week, 0, getdate()), 0);

SELECT TOP (50) [RowIndex]
      ,[Server]
      ,[LogDate]
      ,[IsError]
      ,[UpdateSet]
      ,[Marker]
      ,[Message]
  FROM [KODIAK].[BABW_Interactive_Self_Updater].[dbo].[UpdateLog]
  WHERE IsError = 'N'
  AND UpdateSet != 0
  AND LogDate > @start_of_week
  ORDER BY 3 ASC


POS,spMergeProductCatalogMasterAttributesStage,CREATE proc [POS].[spMergeProductCatalogMasterAttributesStage]
as 

set nocount on 


merge into pos.ProductCatalogMasterAttributesStage as target
using pos.ProductCatalogMasterAttributesPreStage as source
on 
	target.StyleCode=source.StyleCode
	and target.ProductSellingGeography=source.ProductSellingGeography
when matched  then update
	set 
		target.AccessoryType = source.AccessoryType,	
		target.AnimalSoldSeparately = source.AnimalSoldSeparately,	
		target.AsthmaFriendly = source.AsthmaFriendly,	
		target.ColorCode = source.ColorCode,	
		target.LicensedCollection = source.LicensedCollection,	
		target.BirthCertificateRequired = source.BirthCertificateRequired,	
		target.BodyType = source.BodyType,	
		 target.Bottoms= source.Bottoms,	
		 target.Boy= source.Boy,
		 target.CommodityCode= source.CommodityCode,	
		 target.Department= source.Department,	
		 target.DisplayOnAmazon= source.DisplayOnAmazon,	
		 target.EyeColor= source.EyeColor,	
		 target.WebExclusive= source.WebExclusive,	
		 target.Girl= source.Girl,	
		 target.Neutral= source.Neutral,	
		 target.Outfits= source.Outfits,	
		 target.GiftBoxType= source.GiftBoxType,	
		 target.KeyStory= source.KeyStory,	
		 target.ManufacturerCountry= source.ManufacturerCountry,	
		 target.MerchInDate= source.MerchInDate,	
		 target.Mini= source.Mini,	
		 target.Music= source.Music,	
		 target.NoInternationalShipping= source.NoInternationalShipping,	
		 target.SAC= source.SAC,	
		 target.SNC= source.SNC,	
		 target.ProductSellingGeography= source.ProductSellingGeography,	
		 target.QuantityRestriction= source.QuantityRestriction,	
		 target.RefundEligible= source.RefundEligible,	
		 target.Seasonal= source.Seasonal,	
		 target.ThirdPartySiteEligible= source.ThirdPartySiteEligible,	
		 target.ShippingClass= source.ShippingClass,	
		 target.Stuffable= source.Stuffable,	
		 target.Tops= source.Tops,	
		 target.WarningLabel= source.WarningLabel,	
		 target.AccessoryEligible= source.AccessoryEligible,	
		 target.SkinType= source.SkinType,	
		 target.FriendHeight= source.FriendHeight,	
		 target.FriendWeight= source.FriendWeight,	
		 target.SoundEligible= source.SoundEligible,	
		 target.MSTAT= source.MSTAT,	
		 target.EmbroideryProductList= source.EmbroideryProductList,	
		 target.ProductCanBeEmbroidered= source.ProductCanBeEmbroidered,	
		 target.ProductMustBeEmbroidered= source.ProductMustBeEmbroidered,	
		 target.UPC= source.UPC,	
		 target.Purses= source.Purses,	
		 target.LICEN= source.LICEN,	
		 target.OnOrderFlag= source.OnOrderFlag,	
		 target.sportsTeam= source.sportsTeam,	
		 target.occasion= source.occasion,	
		 target.giftCardType= source.giftCardType,	
		 target.OccasionCode= source.OccasionCode,	
		 target.PackageOption= source.PackageOption,	
		 target.Web= source.Web,	
		 target.BRF= source.BRF,	
		 target.Inline= source.Inline,	
		 target.AvailB= source.AvailB,	
		 target.BaseID= source.BaseID,	
		 target.Shoes= source.Shoes,	
		 target.Sound= source.Sound,	
		 target.fourLeggedAnimal= source.fourLeggedAnimal,	
		 target.merchOutDate= source.merchOutDate,	
		 target.MLBTeams= source.MLBTeams,	
		 target.NBATeams= source.NBATeams,	
		 target.NFLTeams= source.NFLTeams,	
		 target.NHLTeams= source.NHLTeams,	
		 target.UKFootball= source.UKFootball,	
		 target.isEndlessAisleEligible= source.isEndlessAisleEligible,	
		 target.isTaxExempt= source.isTaxExempt,	
		 target.isCouponEligible= source.isCouponEligible,	
		 target.isEmployeeDiscountEligible= source.isEmployeeDiscountEligible,	
		 target.isLoyaltyRewardsDiscountEligible= source.isLoyaltyRewardsDiscountEligible,	
		 target.isReturnEligible= source.isReturnEligible,	
		 target.ItemDescription= source.ItemDescription,	
		 target.ProductDescription= source.ProductDescription,	
		 target.ItemName= source.ItemName,	
		 target.isCashierEnterQty= source.isCashierEnterQty,	
		 target.isCashierEntersPrice= source.isCashierEntersPrice,	
		 target.isQtyRestricted= source.isQtyRestricted,	
		 target.ProductNumber= source.ProductNumber,	
		 target.ProductCountry= source.ProductCountry,	
		 target.StoreFrontEligible= source.StoreFrontEligible,	
		 target.Class= source.Class,	
		 target.SubClass= source.SubClass,	
		 target.DepartmentCode= source.DepartmentCode,	
		target.ClassCode = source.ClassCode,	
		target.SubClassCode = source.SubClassCode,	
		target.StyleCode = source.StyleCode,	
		target.DepartmentHierarchyGroupID = source.DepartmentHierarchyGroupID,	
		target.ClassHierarchyGroupID = source.ClassHierarchyGroupID,	
		target.SubClassHierarchyGroupID = source.SubClassHierarchyGroupID,	
		target.ClassParentGroupID = source.ClassParentGroupID,	
		target.SubClassParentGroupID = source.SubClassParentGroupID,	
		target.StyleParentGroupID = source.StyleParentGroupID,	
		target.SellingStatus = source.SellingStatus,	
		target.ItemType = source.ItemType,	
		target.tax_item_group_id = source.tax_item_group_id,	
		target.tax_item_group_code = source.tax_item_group_code,	
		target.tax_item_group_description = source.tax_item_group_description,
		target.isWebEligible=source.isWebEligible,
		target.Chain=source.Chain,	
		target.Division=source.Division,
		target.ChainCode=source.ChainCode,
		target.DivisionCode=source.DivisionCode,	
		target.ConsumerGroup=source.ConsumerGroup,
		target.DistributionMultiple=source.DistributionMultiple,
		target.OrderMultiple=source.OrderMultiple,
		target.InnerCasePack=source.InnerCasePack,
		target.CompSetName=source.CompSetName,	
		target.InventoryBuffer=source.InventoryBuffer,
		target.OMSTAT=source.OMSTAT,
		target.WMSTAT=source.WMSTAT,
		target.ONOTE=source.ONOTE, 
		target.ODATE=source.ODATE,
		target.isBundleSKU=source.isBundleSKU,
		target.Outlet=source.Outlet 
when not matched by target then insert
	(
		AccessoryType,	
		AnimalSoldSeparately,	
		AsthmaFriendly,	
		ColorCode,	
		LicensedCollection,	
		BirthCertificateRequired,	
		BodyType,	
		Bottoms,	
		Boy,
		CommodityCode,	
		Department,	
		DisplayOnAmazon,	
		EyeColor,	
		WebExclusive,	
		Girl,	
		Neutral,	
		Outfits,	
		GiftBoxType,	
		KeyStory,	
		ManufacturerCountry,	
		MerchInDate,	
		Mini,	
		Music,	
		NoInternationalShipping,	
		SAC,	
		SNC,	
		ProductSellingGeography,	
		QuantityRestriction,	
		RefundEligible,	
		Seasonal,	
		ThirdPartySiteEligible,	
		ShippingClass,	
		Stuffable,	
		Tops,	
		WarningLabel,	
		AccessoryEligible,	
		SkinType,	
		FriendHeight,	
		FriendWeight,	
		SoundEligible,	
		MSTAT,	
		EmbroideryProductList,	
		ProductCanBeEmbroidered,	
		ProductMustBeEmbroidered,	
		UPC,	
		Purses,	
		LICEN,	
		OnOrderFlag,	
		sportsTeam,	
		occasion,	
		giftCardType,	
		OccasionCode,	
		PackageOption,	
		Web,	
		BRF,	
		Inline,	
		AvailB,	
		BaseID,	
		Shoes,	
		Sound,	
		fourLeggedAnimal,	
		merchOutDate,	
		MLBTeams,	
		NBATeams,	
		NFLTeams,	
		NHLTeams,	
		UKFootball,	
		isEndlessAisleEligible,	
		isTaxExempt,	
		isCouponEligible,	
		isEmployeeDiscountEligible,	
		isLoyaltyRewardsDiscountEligible,	
		isReturnEligible,	
		ItemDescription,	
		ProductDescription,	
		ItemName,	
		isCashierEnterQty,	
		isCashierEntersPrice,	
		isQtyRestricted,	
		ProductNumber,	
		ProductCountry,	
		StoreFrontEligible,	
		Class,	
		SubClass,	
		DepartmentCode,	
		ClassCode,	
		SubClassCode,	
		StyleCode,	
		DepartmentHierarchyGroupID,	
		ClassHierarchyGroupID,	
		SubClassHierarchyGroupID,	
		ClassParentGroupID,	
		SubClassParentGroupID,	
		StyleParentGroupID,	
		SellingStatus,	
		ItemType,	
		tax_item_group_id,	
		tax_item_group_code,	
		tax_item_group_description,
		isWebEligible,
		Chain,	
		Division,
		ChainCode,
		DivisionCode,
		ConsumerGroup,
		DistributionMultiple,
		OrderMultiple,
		InnerCasePack,
		CompSetName,
		InventoryBuffer,
		OMSTAT,
		WMSTAT,
		ONOTE,
		ODATE,
		isBundleSKU,
		Outlet 
	)
values 
	(
		source.AccessoryType,	
		source.AnimalSoldSeparately,	
		source.AsthmaFriendly,	
		source.ColorCode,	
		source.LicensedCollection,	
		source.BirthCertificateRequired,	
		source.BodyType,	
		source.Bottoms,	
		source.Boy,
		source.CommodityCode,	
		source.Department,	
		source.DisplayOnAmazon,	
		source.EyeColor,	
		source.WebExclusive,	
		source.Girl,	
		source.Neutral,	
		source.Outfits,	
		source.GiftBoxType,	
		source.KeyStory,	
		source.ManufacturerCountry,	
		source.MerchInDate,	
		source.Mini,	
		source.Music,	
		source.NoInternationalShipping,	
		source.SAC,	
		source.SNC,	
		source.ProductSellingGeography,	
		source.QuantityRestriction,	
		source.RefundEligible,	
		source.Seasonal,	
		source.ThirdPartySiteEligible,	
		source.ShippingClass,	
		source.Stuffable,	
		source.Tops,	
		source.WarningLabel,	
		source.AccessoryEligible,	
		source.SkinType,	
		source.FriendHeight,	
		source.FriendWeight,	
		source.SoundEligible,	
		source.MSTAT,	
		source.EmbroideryProductList,	
		source.ProductCanBeEmbroidered,	
		source.ProductMustBeEmbroidered,	
		source.UPC,	
		source.Purses,	
		source.LICEN,	
		source.OnOrderFlag,	
		source.sportsTeam,	
		source.occasion,	
		source.giftCardType,	
		source.OccasionCode,	
		source.PackageOption,	
		source.Web,	
		source.BRF,	
		source.Inline,	
		source.AvailB,	
		source.BaseID,	
		source.Shoes,	
		source.Sound,	
		source.fourLeggedAnimal,	
		source.merchOutDate,	
		source.MLBTeams,	
		source.NBATeams,	
		source.NFLTeams,	
		source.NHLTeams,	
		source.UKFootball,	
		source.isEndlessAisleEligible,	
		source.isTaxExempt,	
		source.isCouponEligible,	
		source.isEmployeeDiscountEligible,	
		source.isLoyaltyRewardsDiscountEligible,	
		source.isReturnEligible,	
		source.ItemDescription,	
		source.ProductDescription,	
		source.ItemName,	
		source.isCashierEnterQty,	
		source.isCashierEntersPrice,	
		source.isQtyRestricted,	
		source.ProductNumber,	
		source.ProductCountry,	
		source.StoreFrontEligible,	
		source.Class,	
		source.SubClass,	
		source.DepartmentCode,	
		source.ClassCode,	
		source.SubClassCode,	
		source.StyleCode,	
		source.DepartmentHierarchyGroupID,	
		source.ClassHierarchyGroupID,	
		source.SubClassHierarchyGroupID,	
		source.ClassParentGroupID,	
		source.SubClassParentGroupID,	
		source.StyleParentGroupID,	
		source.SellingStatus,	
		source.ItemType,	
		source.tax_item_group_id,	
		source.tax_item_group_code,	
		source.tax_item_group_description,
		source.isWebEligible,
		source.Chain,	
		source.Division,
		source.ChainCode,
		source.DivisionCode,
		source.ConsumerGroup,
		source.DistributionMultiple,
		source.OrderMultiple,
		source.InnerCasePack,
		source.CompSetName,
		source.InventoryBuffer,
		source.OMSTAT,
		source.WMSTAT,
		source.ONOTE, 
		source.ODATE,
		source.isBundleSku,
		source.Outlet


	)	
when not matched by source then delete ;
POS,spMergeProductImageURL,CREATE proc [POS].[spMergeProductImageURL]

as

set nocount on
;
merge into POS.ProductImageURL as target
using 
	(	
		select  
			cast(right(concat(cast('000000' as varchar), cast(s.ProductCode as varchar)),6) as varchar(6)) as ItemNumber,
			MAX('https://www.buildabear.com/dw/image/v2/BBNG_PRD/on/demandware.static/-/Sites-buildabear-master/default/dwb59c16e2/' 
				+ s.ImageName)
			as ImageURL,
			case 
				when s.ImageName like '%al%'
					or s.ImageName like '%atl%'
					then 0
				else 1
			end as isPrimary
		from POS.ProductNameDescriptionImageNameStage s
		group by 
			cast(right(concat(cast('000000' as varchar), cast(s.ProductCode as varchar)),6) as varchar(6)),
			--'https://www.buildabear.com/dw/image/v2/BBNG_PRD/on/demandware.static/-/Sites-buildabear-master/default/dwb59c16e2/' 
			--	+ s.ImageName,
			case 
				when s.ImageName like '%al%'
					or s.ImageName like '%atl%'
					then 0
				else 1
			end
	) as source
on 
	target.ItemNumber=source.ItemNumber
	and 
	target.isPrimary=source.isPrimary
when matched
	and	isnull(target.ImageURL,'x')<>isnull(source.ImageURL,'x')
then update
	set
		target.ImageURL=source.ImageURL
when not matched by target
then insert
	(
		ItemNumber,
		ImageURL,
		isPrimary
	)
values
	(
		source.ItemNumber,
		source.ImageURL,
		source.isPrimary
	)
;


POS,spMergeProductNameDescription,CREATE proc [POS].[spMergeProductNameDescription]

as

set nocount on

merge into POS.ProductNameDescription as target
using
	(
		select 
			cast(s.ProductCode as int) as PrimaryID,
			cast(right(concat(cast('000000' as varchar), cast(s.ProductCode as varchar)),6) as varchar(6)) as LocalProductCode,
			max(s.DisplayName) DisplayName,
			max(s.Description) Description
		from POS.ProductNameDescriptionImageNameStage s
		where DisplayName not like '%[â¢ÂÃé]%'
		group by 
			cast(s.ProductCode as int),
			cast(right(concat(cast('000000' as varchar), cast(s.ProductCode as varchar)),6) as varchar(6))
			--s.DisplayName,
			--s.Description
	) as source
on 
	target.PrimaryID=source.PrimaryID
	and 
	target.LocalProductCode=source.LocalProductCode
when matched
	and
		isnull(target.DisplayName,'x')<>isnull(source.DisplayName,'x')
		or
		isnull(target.Description,'x')<>isnull(source.Description,'x')
then update
	set 
		target.DisplayName=source.DisplayName,
		target.Description=source.Description
when not matched by target
then insert
	(
		PrimaryID,
		LocalProductCode,
		DisplayName,
		Description
	)
values
	(
		source.PrimaryID,
		source.LocalProductCode,
		source.DisplayName,
		source.Description
	)
;
POS,spMergeProductsOutOfStock,create proc POS.spMergeProductsOutOfStock 

as 

set nocount on

select 
	o.TransactionID, max(o.OrderNum) OrderNum
into #MaxOrder
from [bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.Orders o with (nolock) 
join [bearcluster01.sql.buildabear.com].WebOrderProcessing.WM.OrderStatus os with (nolock) 
	on o.OrderID=os.OrderID 
	and os.CurrentStatus=1 
	and os.[Status] not in ('Cancelled', 'Complete', 'Shipped')
where isnull(PickupStore,'') <> ''
group by o.TransactionID

select 
	right(o.SourceSite,'2') as Country,
	oi.sku ItemNumber, 
	sum(oi.qty) ItemQty
into #Unshipped
from [bearcluster01.sql.buildabear.com].WebOrderProcessing.WM.Orders o with (nolock)
join #MaxOrder mo 
	on mo.TransactionID=o.TransactionID
	and mo.OrderNum=o.OrderNum
join [bearcluster01.sql.buildabear.com].WebOrderProcessing.WM.OrderStatus os with (nolock) 
	on o.OrderID=os.OrderID 
	and os.CurrentStatus=1 
	and os.[Status] not in ('Cancelled', 'Complete', 'Shipped')
join [bearcluster01.sql.buildabear.com].WebOrderProcessing.WM.OrderItems oi with (nolock) on o.OrderID=oi.OrderID
where 1=1
and isnull(o.PickUpStore,'') in ('', '2013','0013')
and len(oi.sku) = 6
group by 
	right(o.SourceSite,'2'),
	oi.sku


	
select 
	SellingGeography,
	StyleCode,
	sum(Qty) Qty
into #Inv
from web.InventoryFact with (nolock)
where LocationCode in ('0013','2013')
group by SellingGeography,
	StyleCode


select 
	i.SellingGeography,
	i.StyleCode
	--i.Qty,
	--u.ItemQty as UnshippedQty,
	--i.Qty-u.ItemQty as ActualQty,
	--case when i.Qty-u.ItemQty <=0 then 1 else 0 end as isOutOfStock 
into #OutOfStock
from #Inv i
join #Unshipped u
	on i.SellingGeography=u.Country
	and i.StyleCode=u.ItemNumber
where i.Qty-u.ItemQty <=0




update p 
set p.isOutOfStock=1
from pos.ProductCatalogMasterAttributesStage p
join #OutOfStock o 
	on p.ProductCountry=o.SellingGeography
	and p.StyleCode=o.StyleCode

update p 
set p.isOutOfStock=1
from pos.PBIProductCatalogMasterAttributesStage p
join #OutOfStock o 
	on p.ProductCountry=o.SellingGeography
	and p.StyleCode=o.StyleCode
```

