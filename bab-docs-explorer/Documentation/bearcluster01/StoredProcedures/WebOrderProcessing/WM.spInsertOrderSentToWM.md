# WM.spInsertOrderSentToWM

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spInsertOrderSentToWM"]
    WM_OrdersSentToWM(["WM.OrdersSentToWM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WM.OrdersSentToWM |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [WM].[spInsertOrderSentToWM] @OrderNumber varchar(10), @OrderSendTime datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	INSERT INTO [WebOrderProcessing].[WM].[OrdersSentToWM] (OrderNum,SendTime)
	VALUES (@OrderNumber, @OrderSendTime)
END

WM,spMergeOMSCustomOrderExport,CREATE proc [WM].[spMergeOMSCustomOrderExport]

as 

set nocount on
;
with
Files as
(
	select distinct ImportFileName 
	from wm.OMSCustomOrderExportStage
)
delete t
from wm.OMSCustomOrderExport t
join Files f on f.ImportFileName=t.ImportFileName
;

merge into wm.OMSCustomOrderExport as target
using wm.OMSCustomOrderExportStage as source
on 
	target.ImportFileName=source.ImportFileName
--when matched 
--	then delete
when not matched by target
	then insert
		(
			TransactionID,	
			OrderNumber,	
			OrderStatus,	
			OrderDateUTC,	
			OrderNetTotal,	
			OrderCustom1,	
			OrderCustom2,	
			OrderCustom3,	
			OrderCustom4,	
			OrderCustom5,	
			DeckSKU,	
			UPC,	
			ItemPrice,	
			OrderItemCustom1,	
			OrderItemCustom2,	
			OrderItemCustom3,	
			OrderItemCustom4,	
			OrderItemCustom5,	
			OrderItemStatusChangeDateUTC,	
			ItemStatus,	
			OrderItemTypeName,	
			OrderDiscount,	
			ItemDiscount,	
			Amount,	
			ItemSubtotal,	
			ItemTotal,	
			GiftCardNumber,	
			GiftCardTypeName,	
			ToName,	
			ToEmail,	
			FromName,	
			FromEmail,	
			Message,	
			GiftCardActivatedAmount,
			ImportFileName,	
			SiteCode,
			Channel,
			InsertDate
		)
	values
		(
			source.TransactionID,	
			source.OrderNumber,	
			source.OrderStatus,	
			source.OrderDateUTC,	
			source.OrderNetTotal,	
			source.OrderCustom1,	
			source.OrderCustom2,	
			source.OrderCustom3,	
			source.OrderCustom4,	
			source.OrderCustom5,	
			source.DeckSKU,
			source.UPC,	
			source.ItemPrice,	
			source.OrderItemCustom1,	
			source.OrderItemCustom2,	
			source.OrderItemCustom3,	
			source.OrderItemCustom4,	
			source.OrderItemCustom5,	
			source.OrderItemStatusChangeDateUTC,	
			source.ItemStatus,	
			source.OrderItemTypeName,	
			source.OrderDiscount,	
			source.ItemDiscount,	
			source.Amount,	
			source.ItemSubtotal,	
			source.ItemTotal,	
			source.GiftCardNumber,	
			source.GiftCardTypeName,	
			source.ToName,	
			source.ToEmail,	
			source.FromName,	
			source.FromEmail,	
			source.Message,	
			source.GiftCardActivatedAmount,
			source.ImportFileName,	
			source.SiteCode,
			source.Channel,
			getdate()
		)
;

WM,spMergeProductCatalogMasterAttributes_Mirror,CREATE proc [WM].[spMergeProductCatalogMasterAttributes_Mirror] 

as 

--------------------------------------------------------------------------------------------------------------------------------
--Dan Tweedie	2018-11-01	Created Proc - Source table is stl-ssis-p-01.IntegrationStaging.Web.ProductCatalogMasterAttributes. 
--											WebOrderProcessing.WM.ProductCatalogMasterAttributes_Mirror is local mirror of source table, 
--											-> updated via ssis that updates source table
--------------------------------------------------------------------------------------------------------------------------------


set nocount on

Merge into WM.ProductCatalogMasterAttributes_Mirror as target
Using 
	(
		select *
		from WM.ProductCatalogMasterAttributes_MirrorStage
		where (UPC is not NULL
				OR
					(UPC is NULL and StoreFrontEligible = 0)
				)
	) as source
On (target.Style_Code = source.Style_Code)
When Matched 
	AND 
		(
				isnull(target.DisplayName,'xxx') <> isnull(source.DisplayName,'xxx')
			OR  isnull(target.ShortDescription, 'xxx') <> isnull(source.ShortDescription, 'xxx')
			OR	isnull(target.UPC,'xxx') <> isnull(source.UPC,'xxx')
			OR	isnull(target.DefaultDisplayName,'xxx') <> isnull(source.DefaultDisplayName,'xxx')
			OR	isnull(target.AccessoryType,'xxx') <> isnull(source.AccessoryType,'xxx')
			OR	isnull(target.AnimalSoldSeparately,'xxx') <> isnull(source.AnimalSoldSeparately,'xxx')
			OR	isnull(target.AsthmaFriendly,'xxx') <> isnull(source.AsthmaFriendly,'xxx')
			OR	isnull(target.ColorCode,'xxx') <> isnull(source.ColorCode,'xxx')
			OR	isnull(target.LicensedCollection,'xxx') <> isnull(source.LicensedCollection,'xxx')
			OR	isnull(target.BABWProductID,'xxx') <> isnull(source.BABWProductID,'xxx')
			OR	isnull(target.BirthCertificateRequired,'xxx') <> isnull(source.BirthCertificateRequired,'xxx')
			OR	isnull(target.BodyType,'xxx') <> isnull(source.BodyType,'xxx')
			OR	isnull(target.Bottoms,'xxx') <> isnull(source.Bottoms,'xxx')
			OR	isnull(target.Boy,'xxx') <> isnull(source.Boy,'xxx')
			OR	isnull(target.ClassName,'xxx') <> isnull(source.ClassName,'xxx')
			OR	isnull(target.CommodityCode,'xxx') <> isnull(source.CommodityCode,'xxx')
			OR	isnull(target.Department,'xxx') <> isnull(source.Department,'xxx')
			OR  isnull(target.DepartmentSortOrder, 999) <> isnull(source.DepartmentSortOrder,999)
			OR	isnull(target.DisplayOnAmazon,'xxx') <> isnull(source.DisplayOnAmazon,'xxx')
			OR	isnull(target.EyeColor,'xxx') <> isnull(source.EyeColor,'xxx')
			OR	isnull(target.WebExclusive,'xxx') <> isnull(source.WebExclusive,'xxx')
			OR	isnull(target.Girl,'xxx') <> isnull(source.Girl,'xxx')
			OR	isnull(target.Neutral,'xxx') <> isnull(source.Neutral,'xxx')
			OR	isnull(target.Outfits,'xxx') <> isnull(source.Outfits,'xxx')
			OR	isnull(target.GiftBoxType,'xxx') <> isnull(source.GiftBoxType,'xxx')
			OR	isnull(target.HierarchyGroupCode,'xxx') <> isnull(source.HierarchyGroupCode,'xxx')
			OR	isnull(target.KeyStory,'xxx') <> isnull(source.KeyStory,'xxx')
			OR	isnull(target.ManufacturerCountry,'xxx') <> isnull(source.ManufacturerCountry,'xxx')
			OR	isnull(target.MerchInDate,'1900-01-01') <> isnull(source.MerchInDate,'1900-01-01')
			OR	isnull(target.Mini,'xxx') <> isnull(source.Mini,'xxx')
			OR	isnull(target.Music,'xxx') <> isnull(source.Music,'xxx')
			OR	isnull(target.NoInternationalShipping,'xxx') <> isnull(source.NoInternationalShipping,'xxx')
			OR	isnull(target.SAC,'xxx') <> isnull(source.SAC,'xxx')
			OR	isnull(target.SNC,'xxx') <> isnull(source.SNC,'xxx')
			OR	isnull(target.ProductSellingGeography,'xxx') <> isnull(source.ProductSellingGeography,'xxx')
			OR	isnull(target.QuantityRestriction,'999999') <> isnull(source.QuantityRestriction,'999999')
			OR	isnull(target.RefundEligible,'xxx') <> isnull(source.RefundEligible,'xxx')
			OR	isnull(target.Seasonal,'xxx') <> isnull(source.Seasonal,'xxx')
			OR	isnull(target.ThirdPartySiteEligible,'xxx') <> isnull(source.ThirdPartySiteEligible,'xxx')
			OR	isnull(target.ShippingClass,'xxx') <> isnull(source.ShippingClass,'xxx')
			OR	isnull(target.Stuffable,'xxx') <> isnull(source.Stuffable,'xxx')
			OR	isnull(target.Tops,'xxx') <> isnull(source.Tops,'xxx')
			OR	isnull(target.WarningLabel,'xxx') <> isnull(source.WarningLabel,'xxx')
			OR	isnull(target.AccessoryEligible,'xxx') <> isnull(source.AccessoryEligible,'xxx')
			OR	isnull(target.SkinType,'xxx') <> isnull(source.SkinType,'xxx')
			OR	isnull(target.FriendHeight,'xxx') <> isnull(source.FriendHeight,'xxx')
			OR	isnull(target.FriendWeight,'xxx') <> isnull(source.FriendWeight,'xxx')
			OR	isnull(target.SoundEligible,'xxx') <> isnull(source.SoundEligible,'xxx')
			OR	isnull(target.MSTAT,'xxx') <> isnull(source.MSTAT,'xxx')
			OR	isnull(target.EmbroideryProductList,'xxx') <> isnull(source.EmbroideryProductList,'xxx')
			OR	isnull(target.ProductCanBeEmbroidered,'xxx') <> isnull(source.ProductCanBeEmbroidered,'xxx')
			OR	isnull(target.ProductMustBeEmbroidered,'xxx') <> isnull(source.ProductMustBeEmbroidered,'xxx')
			OR	isnull(target.Purses,'xxx') <> isnull(source.Purses,'xxx')
			OR	isnull(target.EnableEmailAFriend,'xxx') <> isnull(source.EnableEmailAFriend,'xxx')
			OR	isnull(target.CopyStatus,'xxx') <> isnull(source.CopyStatus,'xxx')
			OR	isnull(target.GoogleTag1,'xxx') <> isnull(source.GoogleTag1,'xxx')
			OR	isnull(target.GoogleTag2,'xxx') <> isnull(source.GoogleTag2,'xxx')
			OR	isnull(target.GoogleTag3,'xxx') <> isnull(source.GoogleTag3,'xxx')
			OR	isnull(target.GoogleTag4,'xxx') <> isnull(source.GoogleTag4,'xxx')
			OR	isnull(target.GoogleTag5,'xxx') <> isnull(source.GoogleTag5,'xxx')
			OR	isnull(target.NewProduct,'xxx') <> isnull(source.NewProduct,'xxx')
			OR	isnull(target.PrimaryCategoryDerived,'xxx') <> isnull(source.PrimaryCategoryDerived,'xxx')
			OR	isnull(target.ChildSKUs,'xxx') <> isnull(source.ChildSKUs,'xxx')
			OR	isnull(target.DisplayableSkuAttributes,'xxx') <> isnull(source.DisplayableSkuAttributes,'xxx')
			OR	isnull(target.PreOrderable,'xxx') <> isnull(source.PreOrderable,'xxx')
			OR	isnull(target.PreorderEndDate,'1900-01-01') <> isnull(source.PreorderEndDate,'1900-01-01')
			OR	isnull(target.DefaultKeywords,'xxx') <> isnull(source.DefaultKeywords,'xxx')
			OR	isnull(target.CategoryTree,'xxx') <> isnull(source.CategoryTree,'xxx')
			OR	isnull(target.LICEN,'xxx') <> isnull(source.LICEN,'xxx')
			OR  isnull(target.sportsTeam,'xxx') <> isnull(source.sportsTeam,'xxx')
			OR  isnull(target.OccasionCode, 'xxx') <> isnull(source.OccasionCode,'xxx')
			OR  isnull(target.StoreFrontEligible, 99) <> isnull(source.StoreFrontEligible, 99)
			OR  isnull(target.OnOrderFlag,99) <> isnull(source.OnOrderFlag,99)
			OR  isnull(target.InventoryBuffer,99) <> isnull(source.InventoryBuffer,99)
			OR  isnull(target.Inventory,123456789) <> isnull(source.Inventory,123456789)
			OR  isnull(target.OnlineFlag,99) <> isnull(source.OnlineFlag,99)
			OR  isnull(target.SearchableFlag,99) <> isnull(source.SearchableFlag,99)
			OR  isnull(target.SearchableIfUnavailableFlag,99) <> isnull(source.SearchableIfUnavailableFlag,99)
			OR  isnull(target.giftCardType, 'X') <> isnull(source.giftCardType,'X')
			OR  isnull(target.PackageOption,'x') <> isnull(source.PackageOption,'x')
			OR  isnull(target.dropShipCustLines,0) <> isnull(source.dropShipCustLines,0)
			OR  isnull(target.isCPS,3) <> isnull(source.isCPS,3)
		)
	Then 
		Update 
			Set 
				target.DisplayName	=	source.DisplayName,
				target.ShortDescription =	source.ShortDescription,
				target.UPC	=	source.UPC,
				target.DefaultDisplayName	=	source.DefaultDisplayName,
				target.AccessoryType	=	source.AccessoryType,
				target.AnimalSoldSeparately	=	source.AnimalSoldSeparately,
				target.AsthmaFriendly	=	source.AsthmaFriendly,
				target.ColorCode	=	source.ColorCode,
				target.LicensedCollection	=	source.LicensedCollection,
				target.BABWProductID	=	source.BABWProductID,
				target.BirthCertificateRequired	=	source.BirthCertificateRequired,
				target.BodyType	=	source.BodyType,
				target.Bottoms	=	source.Bottoms,
				target.Boy	=	source.Boy,
				target.ClassName	=	source.ClassName,
				target.CommodityCode	=	source.CommodityCode,
				target.Department	=	source.Department,
				target.DepartmentSortOrder = source.DepartmentSortOrder,
				target.DisplayOnAmazon	=	source.DisplayOnAmazon,
				target.EyeColor	=	source.EyeColor,
				target.WebExclusive	=	source.WebExclusive,
				target.Girl	=	source.Girl,
				target.Neutral	=	source.Neutral,
				target.Outfits	=	source.Outfits,
				target.GiftBoxType	=	source.GiftBoxType,
				target.HierarchyGroupCode	=	source.HierarchyGroupCode,
				target.KeyStory	=	source.KeyStory,
				target.ManufacturerCountry	=	source.ManufacturerCountry,
				target.MerchInDate	=	source.MerchInDate,
				target.Mini	=	source.Mini,
				target.Music	=	source.Music,
				target.NoInternationalShipping	=	source.NoInternationalShipping,
				target.SAC	=	source.SAC,
				target.SNC	=	source.SNC,
				target.ProductSellingGeography	=	source.ProductSellingGeography,
				target.QuantityRestriction	=	source.QuantityRestriction,
				target.RefundEligible	=	source.RefundEligible,
				target.Seasonal	=	source.Seasonal,
				target.ThirdPartySiteEligible	=	source.ThirdPartySiteEligible,
				target.ShippingClass	=	source.ShippingClass,
				target.Stuffable	=	source.Stuffable,
				target.Tops	=	source.Tops,
				target.WarningLabel	=	source.WarningLabel,
				target.AccessoryEligible	=	source.AccessoryEligible,
				target.SkinType	=	source.SkinType,
				target.FriendHeight	=	source.FriendHeight,
				target.FriendWeight	=	source.FriendWeight,
				target.SoundEligible	=	source.SoundEligible,
				target.MSTAT	=	source.MSTAT,
				target.EmbroideryProductList	=	source.EmbroideryProductList,
				target.ProductCanBeEmbroidered	=	source.ProductCanBeEmbroidered,
				target.ProductMustBeEmbroidered	=	source.ProductMustBeEmbroidered,
				target.Purses	=	source.Purses,
				target.EnableEmailAFriend	=	source.EnableEmailAFriend,
				target.CopyStatus	=	source.CopyStatus,
				target.GoogleTag1	=	source.GoogleTag1,
				target.GoogleTag2	=	source.GoogleTag2,
				target.GoogleTag3	=	source.GoogleTag3,
				target.GoogleTag4	=	source.GoogleTag4,
				target.GoogleTag5	=	source.GoogleTag5,
				target.NewProduct	=	source.NewProduct,
				target.PrimaryCategoryDerived	=	source.PrimaryCategoryDerived,
				target.ChildSKUs	=	source.ChildSKUs,
				target.DisplayableSkuAttributes	=	source.DisplayableSkuAttributes,
				target.PreOrderable	=	source.PreOrderable,
				target.PreorderEndDate	=	source.PreorderEndDate,
				target.DefaultKeywords	=	source.DefaultKeywords,
				target.CategoryTree	=	source.CategoryTree,
				target.LICEN	=	source.LICEN,
				target.sportsTeam =		source.sportsTeam,
				target.OccasionCode = source.OccasionCode,
				target.StoreFrontEligible =		source.StoreFrontEligible,
				target.OnOrderFlag =	source.OnOrderFlag,
				target.InventoryBuffer = source.InventoryBuffer,
				target.Inventory = source.Inventory,
				target.OnlineFlag =	source.OnlineFlag,
				target.SearchableFlag =		source.SearchableFlag,
				target.SearchableIfUnavailableFlag =	source.SearchableIfUnavailableFlag,
				target.giftCardType =	source.giftCardType,
				target.PackageOption = source.PackageOption,
				target.dropShipCustLines = source.dropShipCustLines,
				target.isCPS = source.isCPS,
				target.UpdateDate	=	getdate()
When Not Matched By Target 
	Then 
		Insert (
				Style_Code,
				DisplayName,
				ShortDescription,
				UPC,
				DefaultDisplayName,
				AccessoryType,
				AnimalSoldSeparately,
				AsthmaFriendly,
				ColorCode,
				LicensedCollection,
				BABWProductID,
				BirthCertificateRequired,
				BodyType,
				Bottoms,
				Boy,
				ClassName,
				CommodityCode,
				Department,
				DepartmentSortOrder,
				DisplayOnAmazon,
				EyeColor,
				WebExclusive,
				Girl,
				Neutral,
				Outfits,
				GiftBoxType,
				HierarchyGroupCode,
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
				Purses,
				EnableEmailAFriend,
				CopyStatus,
				GoogleTag1,
				GoogleTag2,
				GoogleTag3,
				GoogleTag4,
				GoogleTag5,
				NewProduct,
				PrimaryCategoryDerived,
				ChildSKUs,
				DisplayableSkuAttributes,
				PreOrderable,
				PreorderEndDate,
				DefaultKeywords,
				CategoryTree,
				LICEN,
				sportsTeam,
				OccasionCode,
				StoreFrontEligible,
				OnOrderFlag,
				InventoryBuffer,
				Inventory,
				OnlineFlag,
				SearchableFlag,
				SearchableIfUnavailableFlag,
				giftCardType,
				PackageOption,
				dropShipCustLines,
				isCPS,
				InsertDate
				)
		Values (
					source.Style_Code,
					source.DisplayName,
					source.ShortDescription,
					source.UPC,
					source.DefaultDisplayName,
					source.AccessoryType,
					source.AnimalSoldSeparately,
					source.AsthmaFriendly,
					source.ColorCode,
					source.LicensedCollection,
					source.BABWProductID,
					source.BirthCertificateRequired,
					source.BodyType,
					source.Bottoms,
					source.Boy,
					source.ClassName,
					source.CommodityCode,
					source.Department,
					source.DepartmentSortOrder,
					source.DisplayOnAmazon,
					source.EyeColor,
					source.WebExclusive,
					source.Girl,
					source.Neutral,
					source.Outfits,
					source.GiftBoxType,
					source.HierarchyGroupCode,
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
					source.Purses,
					source.EnableEmailAFriend,
					source.CopyStatus,
					source.GoogleTag1,
					source.GoogleTag2,
					source.GoogleTag3,
					source.GoogleTag4,
					source.GoogleTag5,
					source.NewProduct,
					source.PrimaryCategoryDerived,
					source.ChildSKUs,
					source.DisplayableSkuAttributes,
					source.PreOrderable,
					source.PreorderEndDate,
					source.DefaultKeywords,
					source.CategoryTree,
					source.LICEN,
					source.sportsTeam,
					source.OccasionCode,
					source.StoreFrontEligible,
					source.OnOrderFlag,
					source.InventoryBuffer,
					source.Inventory,
					source.OnlineFlag,
					source.SearchableFlag,
					source.SearchableIfUnavailableFlag,
					source.giftCardType,
					source.PackageOption,
					source.dropShipCustLines,
					source.isCPS,
					getdate()
				)
When Not Matched By Source
	Then
		delete
;
```

