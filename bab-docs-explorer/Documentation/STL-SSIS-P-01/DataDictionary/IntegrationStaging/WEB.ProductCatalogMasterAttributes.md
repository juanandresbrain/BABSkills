# WEB.ProductCatalogMasterAttributes

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Style_Code | varchar | 6 | 1 |  |  |  |
| DisplayName | nvarchar | 300 | 1 |  |  |  |
| ShortDescription | nvarchar | 4000 | 1 |  |  |  |
| UPC | varchar | 20 | 1 |  |  |  |
| DefaultDisplayName | varchar | 150 | 1 |  |  |  |
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
| EnableEmailAFriend | varchar | 5 | 1 |  |  |  |
| CopyStatus | varchar | 150 | 1 |  |  |  |
| GoogleTag1 | varchar | 150 | 1 |  |  |  |
| GoogleTag2 | varchar | 150 | 1 |  |  |  |
| GoogleTag3 | varchar | 150 | 1 |  |  |  |
| GoogleTag4 | varchar | 150 | 1 |  |  |  |
| GoogleTag5 | varchar | 150 | 1 |  |  |  |
| NewProduct | varchar | 150 | 1 |  |  |  |
| PrimaryCategoryDerived | varchar | 150 | 1 |  |  |  |
| ChildSKUs | varchar | 150 | 1 |  |  |  |
| DisplayableSkuAttributes | varchar | 150 | 1 |  |  |  |
| PreOrderable | varchar | 5 | 1 |  |  |  |
| PreorderEndDate | date | 3 | 1 |  |  |  |
| DefaultKeywords | varchar | 150 | 1 |  |  |  |
| CategoryTree | nvarchar | 800 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| LICEN | varchar | 2 | 1 |  |  |  |
| sportsTeam | varchar | 500 | 1 |  |  |  |
| occasion | varchar | 100 | 1 |  |  |  |
| OccasionCode | varchar | 100 | 1 |  |  |  |
| StoreFrontEligible | int | 4 | 1 |  |  |  |
| OnOrderFlag | int | 4 | 1 |  |  |  |
| InventoryBuffer | int | 4 | 1 |  |  |  |
| Inventory | int | 4 | 1 |  |  |  |
| OnlineFlag | int | 4 | 1 |  |  |  |
| SearchableFlag | int | 4 | 1 |  |  |  |
| SearchableIfUnavailableFlag | int | 4 | 1 |  |  |  |
| IsFirstTransmit | int | 4 | 1 |  |  |  |
| giftCardType | varchar | 30 | 1 |  |  |  |
| PackageOption | varchar | 10 | 1 |  |  |  |
| dropShipCustLines | int | 4 | 1 |  |  |  |
| isCPS | bit | 1 | 1 |  |  |  |
| Web | varchar | 10 | 1 |  |  |  |
| WebBuf | int | 4 | 1 |  |  |  |
| BRF | varchar | 10 | 1 |  |  |  |
| Inline | nvarchar | 300 | 1 |  |  |  |
| AvailB | varchar | 6 | 1 |  |  |  |
| WebInStock | varchar | 5 | 1 |  |  |  |
| StoreInStock | varchar | 5 | 1 |  |  |  |
| OriginalRetail | decimal | 9 | 1 |  |  |  |
| CurrentRetail | decimal | 9 | 1 |  |  |  |
| OnOrder | varchar | 5 | 1 |  |  |  |
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

- [IntegrationStaging: WEB.spMergeInventoryFactFromWM](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWM.md)
- [IntegrationStaging: WEB.spMergeInventoryFactFromWMbackup20191208](../../StoredProcedures/IntegrationStaging/WEB.spMergeInventoryFactFromWMbackup20191208.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes.md)
- [IntegrationStaging: WEB.spMergeProductCatalogMasterAttributes_backup20221102](../../StoredProcedures/IntegrationStaging/WEB.spMergeProductCatalogMasterAttributes_backup20221102.md)
- [IntegrationStaging: WEB.spOutputMasterCatalog](../../StoredProcedures/IntegrationStaging/WEB.spOutputMasterCatalog.md)

