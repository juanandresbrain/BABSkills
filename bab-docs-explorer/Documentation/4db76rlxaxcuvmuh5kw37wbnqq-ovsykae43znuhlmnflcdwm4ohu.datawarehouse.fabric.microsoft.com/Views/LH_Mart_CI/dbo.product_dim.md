# dbo.product_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.product_dim"]
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[product_dim] AS     SELECT [product_key], [sku], [activation_date], [style_code] COLLATE Latin1_General_CI_AS AS [style_code], [style_desc] COLLATE Latin1_General_CI_AS AS [style_desc], [color_code] COLLATE Latin1_General_CI_AS AS [color_code], [color_desc] COLLATE Latin1_General_CI_AS AS [color_desc], [product_desc] COLLATE Latin1_General_CI_AS AS [product_desc], [subclass] COLLATE Latin1_General_CI_AS AS [subclass], [class] COLLATE Latin1_General_CI_AS AS [class], [department] COLLATE Latin1_General_CI_AS AS [department], [department_code] COLLATE Latin1_General_CI_AS AS [department_code], [division] COLLATE Latin1_General_CI_AS AS [division], [chain] COLLATE Latin1_General_CI_AS AS [chain], [concept] COLLATE Latin1_General_CI_AS AS [concept], [priceline_code] COLLATE Latin1_General_CI_AS AS [priceline_code], [subclass_code] COLLATE Latin1_General_CI_AS AS [subclass_code], [class_code] COLLATE Latin1_General_CI_AS AS [class_code], [primary_vendor_code] COLLATE Latin1_General_CI_AS AS [primary_vendor_code], [primary_vendor_name] COLLATE Latin1_General_CI_AS AS [primary_vendor_name], [alt_primary_vendor_code] COLLATE Latin1_General_CI_AS AS [alt_primary_vendor_code], [current_retail], [original_retail], [price_with_vat], [reorder_flag], [euro_value], [merch_status] COLLATE Latin1_General_CI_AS AS [merch_status], [wss_reportable] COLLATE Latin1_General_CI_AS AS [wss_reportable], [style_id], [color_id], [current_selling_retail_home], [jurisdiction_code] COLLATE Latin1_General_CI_AS AS [jurisdiction_code], [jurisdiction_id], [cdn_value], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID], [GENDER] COLLATE Latin1_General_CI_AS AS [GENDER], [CORE_FASH_CD] COLLATE Latin1_General_CI_AS AS [CORE_FASH_CD], [INLINE_CD] COLLATE Latin1_General_CI_AS AS [INLINE_CD], [ScorecardCategory] COLLATE Latin1_General_CI_AS AS [ScorecardCategory], [BaseID] COLLATE Latin1_General_CI_AS AS [BaseID], [UPC] COLLATE Latin1_General_CI_AS AS [UPC], [ItemType] COLLATE Latin1_General_CI_AS AS [ItemType], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [RoyaltyType] COLLATE Latin1_General_CI_AS AS [RoyaltyType], [RoyaltyAmount], [RoyaltyPercent], [TotalFOB], [CNDescription] COLLATE Latin1_General_CI_AS AS [CNDescription], [SellingStatus] COLLATE Latin1_General_CI_AS AS [SellingStatus], [giftCardType] COLLATE Latin1_General_CI_AS AS [giftCardType], [AccessoryType] COLLATE Latin1_General_CI_AS AS [AccessoryType], [LicensedCollection] COLLATE Latin1_General_CI_AS AS [LicensedCollection], [LICEN] COLLATE Latin1_General_CI_AS AS [LICEN], [LICEN2], [Licensor] COLLATE Latin1_General_CI_AS AS [Licensor], [DepartmentSortOrder], [PlushEyeColor] COLLATE Latin1_General_CI_AS AS [PlushEyeColor], [PlushFurColor] COLLATE Latin1_General_CI_AS AS [PlushFurColor], [PlushHeight], [PlushWeight] COLLATE Latin1_General_CI_AS AS [PlushWeight], [WebExclusive], [Silhouette] COLLATE Latin1_General_CI_AS AS [Silhouette], [Outfits] COLLATE Latin1_General_CI_AS AS [Outfits], [ItemGroupID] COLLATE Latin1_General_CI_AS AS [ItemGroupID], [Category1] COLLATE Latin1_General_CI_AS AS [Category1], [Category2] COLLATE Latin1_General_CI_AS AS [Category2], [ProductCategory] COLLATE Latin1_General_CI_AS AS [ProductCategory], [FloorSet] COLLATE Latin1_General_CI_AS AS [FloorSet], [COO] COLLATE Latin1_General_CI_AS AS [COO], [COO_Desc] COLLATE Latin1_General_CI_AS AS [COO_Desc], [InDate], [OutDate], [WarningHangtag] COLLATE Latin1_General_CI_AS AS [WarningHangtag], [SportsTeams] COLLATE Latin1_General_CI_AS AS [SportsTeams], [ModelGroupID] COLLATE Latin1_General_CI_AS AS [ModelGroupID], [BarcodeType] COLLATE Latin1_General_CI_AS AS [BarcodeType], [isEndlessAisleEligible] COLLATE Latin1_General_CI_AS AS [isEndlessAisleEligible], [HTSCode] COLLATE Latin1_General_CI_AS AS [HTSCode], [HTSCodeDesc] COLLATE Latin1_General_CI_AS AS [HTSCodeDesc], [US_HTS_Code] COLLATE Latin1_General_CI_AS AS [US_HTS_Code], [CAN_HTS_Code] COLLATE Latin1_General_CI_AS AS [CAN_HTS_Code], [UK_HTS_Code] COLLATE Latin1_General_CI_AS AS [UK_HTS_Code], [TaxItemGroupCode] COLLATE Latin1_General_CI_AS AS [TaxItemGroupCode]     FROM LH_Mart.[dbo].[product_dim]
```

