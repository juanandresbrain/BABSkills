# dbo.WebProductCatalogMasterAttributes

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Style_Code | varchar | 6 | 1 |  |  |  |
| SKUDescription | nvarchar | 300 | 1 |  |  |  |
| UPC | varchar | 20 | 1 |  |  |  |
| DefaultDisplayName | int | 4 | 1 |  |  |  |
| AccessoryType | nvarchar | 80 | 1 |  |  |  |
| AnimalSoldSeparately | varchar | 5 | 1 |  |  |  |
| AsthmaFriendly | varchar | 5 | 1 |  |  |  |
| ColorCode | nvarchar | 40 | 1 |  |  |  |
| LicensedCollection | nvarchar | 12 | 1 |  |  |  |
| BABWProductID | varchar | 6 | 1 |  |  |  |
| BirthCertificateRequired | varchar | 5 | 1 |  |  |  |
| BodyType | nvarchar | 12 | 1 |  |  |  |
| Bottoms | varchar | 5 | 1 |  |  |  |
| Boy | varchar | 5 | 1 |  |  |  |
| ClassName | nvarchar | 80 | 1 |  |  |  |
| CommodityCode | varchar | 52 | 1 |  |  |  |
| Department | nvarchar | 80 | 1 |  |  |  |
| DepartmentSortOrder | int | 4 | 1 |  |  |  |
| DisplayOnAmazon | varchar | 5 | 1 |  |  |  |
| EyeColor | nvarchar | 12 | 1 |  |  |  |
| WebExclusive | varchar | 5 | 1 |  |  |  |
| Girl | varchar | 5 | 1 |  |  |  |
| Neutral | varchar | 5 | 1 |  |  |  |
| Outfits | varchar | 5 | 1 |  |  |  |
| GiftBoxType | varchar | 7 | 1 |  |  |  |
| HierarchyGroupCode | nvarchar | 40 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| ManufacturerCountry | nvarchar | 12 | 1 |  |  |  |
| MerchInDate | date | 3 | 1 |  |  |  |
| Mini | varchar | 5 | 1 |  |  |  |
| Music | varchar | 5 | 1 |  |  |  |
| NoInternationalShipping | varchar | 5 | 1 |  |  |  |
| SAC | varchar | 5 | 1 |  |  |  |
| SNC | varchar | 5 | 1 |  |  |  |
| ProductSellingGeography | varchar | 2 | 1 |  |  |  |
| QuantityRestriction | int | 4 | 1 |  |  |  |
| RefundEligible | varchar | 5 | 1 |  |  |  |
| Seasonal | varchar | 5 | 1 |  |  |  |
| ThirdPartySiteEligible | varchar | 5 | 1 |  |  |  |
| ShippingClass | varchar | 13 | 1 |  |  |  |
| Stuffable | varchar | 5 | 1 |  |  |  |
| Tops | varchar | 5 | 1 |  |  |  |
| WarningLabel | nvarchar | 12 | 1 |  |  |  |
| AccessoryEligible | varchar | 5 | 1 |  |  |  |
| SkinType | nvarchar | 12 | 1 |  |  |  |
| FriendHeight | nvarchar | 60 | 1 |  |  |  |
| FriendWeight | nvarchar | 60 | 1 |  |  |  |
| SoundEligible | varchar | 5 | 1 |  |  |  |
| MSTAT | nvarchar | 12 | 1 |  |  |  |
| EmbroideryProductList | varchar | 5 | 1 |  |  |  |
| ProductCanBeEmbroidered | varchar | 5 | 1 |  |  |  |
| ProductMustBeEmbroidered | varchar | 5 | 1 |  |  |  |
| Purses | varchar | 5 | 1 |  |  |  |
| EnableEmailAFriend | int | 4 | 1 |  |  |  |
| CopyStatus | int | 4 | 1 |  |  |  |
| GoogleTag1 | int | 4 | 1 |  |  |  |
| GoogleTag2 | int | 4 | 1 |  |  |  |
| GoogleTag3 | int | 4 | 1 |  |  |  |
| GoogleTag4 | int | 4 | 1 |  |  |  |
| GoogleTag5 | int | 4 | 1 |  |  |  |
| NewProduct | int | 4 | 1 |  |  |  |
| PrimaryCategoryDerived | int | 4 | 1 |  |  |  |
| ChildSKUs | int | 4 | 1 |  |  |  |
| DisplayableSkuAttributes | int | 4 | 1 |  |  |  |
| PreOrderable | int | 4 | 1 |  |  |  |
| PreorderEndDate | int | 4 | 1 |  |  |  |
| DefaultKeywords | int | 4 | 1 |  |  |  |
| CategoryTree | nvarchar | 800 | 1 |  |  |  |
| LICEN | varchar | 2 | 1 |  |  |  |
| sportsTeam | varchar | 500 | 1 |  |  |  |
| occasion | varchar | 100 | 1 |  |  |  |
| OccasionCode | varchar | 100 | 1 |  |  |  |
| StorefrontEligible | int | 4 | 1 |  |  |  |
| OnOrderFlag | int | 4 | 1 |  |  |  |
| InventoryBuffer | int | 4 | 1 |  |  |  |
| Searchable | int | 4 | 1 |  |  |  |
| SearchableIfUnavailable | int | 4 | 1 |  |  |  |
| giftCardType | varchar | 30 | 1 |  |  |  |
| PackageOption | varchar | 10 | 1 |  |  |  |
| dropShipCustLines | int | 4 | 1 |  |  |  |
| Web | varchar | 10 | 1 |  |  |  |
| BRF | varchar | 10 | 1 |  |  |  |
| Inline | nvarchar | 300 | 1 |  |  |  |
| AvailB | varchar | 5 | 1 |  |  |  |
| SubClassLabel | varchar | 100 | 1 |  |  |  |
| BaseID | varchar | 6 | 1 |  |  |  |
| Shoes | int | 4 | 1 |  |  |  |
| Sound | int | 4 | 1 |  |  |  |
| fourLeggedAnimal | int | 4 | 1 |  |  |  |
| merchOutDate | date | 3 | 1 |  |  |  |
| MLBTeams | varchar | 100 | 1 |  |  |  |
| NBATeams | varchar | 100 | 1 |  |  |  |
| NFLTeams | varchar | 100 | 1 |  |  |  |
| NHLTeams | varchar | 100 | 1 |  |  |  |
| UKFootball | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spSelectStoreInventoryPrepData](../../StoredProcedures/me_01/dbo.spSelectStoreInventoryPrepData.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes_BackUp20221101](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes_BackUp20221101.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes_backup20221102](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes_backup20221102.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributesBAK20171005](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributesBAK20171005.md)
- [esell: dbo.spSelectEnterpriseSellingInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805.md)
- [esell: dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711](../../StoredProcedures/esell/dbo.spSelectEnterpriseSellingStoreInventoryBAK20220711.md)

