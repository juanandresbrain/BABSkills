# Azure.vwPOSOutbound_Products

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_Products"]
    POS_ProductCatalogMasterAttributesStage(["POS.ProductCatalogMasterAttributesStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| POS.ProductCatalogMasterAttributesStage |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_Products] AS




SELECT [AccessoryType]
      ,[AnimalSoldSeparately]
      ,[AsthmaFriendly]
      ,[ColorCode]
      ,[LicensedCollection]
      ,[BirthCertificateRequired]
      ,[BodyType]
      ,[Bottoms]
      ,[Boy]
      ,[CommodityCode]
      ,[Department]
      ,[DisplayOnAmazon]
      ,[EyeColor]
      ,[WebExclusive]
      ,[Girl]
      ,[Neutral]
      ,[Outfits]
      ,[GiftBoxType]
      ,[KeyStory]
      ,[ManufacturerCountry]
      ,[MerchInDate]
      ,[Mini]
      ,[Music]
      ,[NoInternationalShipping]
      ,[SAC]
      ,[SNC]
      ,[ProductSellingGeography]
      --,[QuantityRestriction]
	  ,999 as QuantityRestriction
      ,[RefundEligible]
      ,[Seasonal]
      ,[ThirdPartySiteEligible]
      ,[ShippingClass]
      ,[Stuffable]
      ,[Tops]
      ,[WarningLabel]
      ,[AccessoryEligible]
      ,[SkinType]
      ,[FriendHeight]
      ,[FriendWeight]
      ,[SoundEligible]
      ,[MSTAT]
      ,[EmbroideryProductList]
      ,[ProductCanBeEmbroidered]
      ,[ProductMustBeEmbroidered]
      ,[UPC]
      ,[Purses]
      ,[LICEN]
      ,[OnOrderFlag]
      ,[sportsTeam]
      ,[occasion]
      ,[giftCardType]
      ,[OccasionCode]
      ,[PackageOption]
      ,[Web]
      ,[BRF]
      ,[Inline]
      ,[AvailB]
      ,[BaseID]
      ,[Shoes]
      ,[Sound]
      ,[fourLeggedAnimal]
      ,[merchOutDate]
      ,[MLBTeams]
      ,[NBATeams]
      ,[NFLTeams]
      ,[NHLTeams]
      ,[UKFootball]
      ,[isEndlessAisleEligible]
      ,[isTaxExempt]
      ,[isCouponEligible]
      ,[isEmployeeDiscountEligible]
      ,[isReturnEligible]
      ,[ItemDescription]
      ,[ProductDescription]
      ,[ItemName]
      ,[isCashierEnterQty]
      ,[isCashierEntersPrice]
      ,[isQtyRestricted]
      ,[ProductNumber]
      ,[ProductCountry]
      ,[StoreFrontEligible]
      ,[Class]
      ,[SubClass]
      ,[DepartmentCode]
      ,[ClassCode]
      ,[SubClassCode]
      ,[StyleCode]
      ,[DepartmentHierarchyGroupID]
      ,[ClassHierarchyGroupID]
      ,[SubClassHierarchyGroupID]
      ,[ClassParentGroupID]
      ,[SubClassParentGroupID]
      ,[StyleParentGroupID]
      ,[SellingStatus]
      ,[ItemType]
      ,[tax_item_group_id]
      ,[tax_item_group_code]
      ,[tax_item_group_description]
	  ,[isLoyaltyRewardsDiscountEligible]
  FROM [stl-ssis-p-01].[IntegrationStaging].[POS].[ProductCatalogMasterAttributesStage]
```

