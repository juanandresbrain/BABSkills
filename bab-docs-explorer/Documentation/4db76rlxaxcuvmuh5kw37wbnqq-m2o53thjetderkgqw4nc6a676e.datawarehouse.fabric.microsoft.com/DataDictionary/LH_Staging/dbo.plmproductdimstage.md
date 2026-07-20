# dbo.plmproductdimstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | bigint | 8 | 1 |  |  |  |
| sku | bigint | 8 | 1 |  |  |  |
| activation_date | datetime2 | 8 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| style_desc | varchar | 8000 | 1 |  |  |  |
| color_code | varchar | 8000 | 1 |  |  |  |
| color_desc | varchar | 8000 | 1 |  |  |  |
| product_desc | varchar | 8000 | 1 |  |  |  |
| subclass | varchar | 8000 | 1 |  |  |  |
| class | varchar | 8000 | 1 |  |  |  |
| department | varchar | 8000 | 1 |  |  |  |
| department_code | varchar | 8000 | 1 |  |  |  |
| division | varchar | 8000 | 1 |  |  |  |
| chain | varchar | 8000 | 1 |  |  |  |
| concept | varchar | 8000 | 1 |  |  |  |
| priceline_code | varchar | 8000 | 1 |  |  |  |
| subclass_code | varchar | 8000 | 1 |  |  |  |
| class_code | varchar | 8000 | 1 |  |  |  |
| primary_vendor_code | varchar | 8000 | 1 |  |  |  |
| primary_vendor_name | varchar | 8000 | 1 |  |  |  |
| alt_primary_vendor_code | varchar | 8000 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| price_with_vat | decimal | 9 | 1 |  |  |  |
| reorder_flag | int | 4 | 1 |  |  |  |
| euro_value | decimal | 9 | 1 |  |  |  |
| merch_status | varchar | 8000 | 1 |  |  |  |
| wss_reportable | int | 4 | 1 |  |  |  |
| current_selling_retail_home | decimal | 9 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| availb | varchar | 8000 | 1 |  |  |  |
| cdn_value | decimal | 9 | 1 |  |  |  |
| GENDER | varchar | 8000 | 1 |  |  |  |
| CORE_FASH_CD | varchar | 8000 | 1 |  |  |  |
| INLINE_CD | varchar | 8000 | 1 |  |  |  |
| ScorecardCategory | varchar | 8000 | 1 |  |  |  |
| BaseID | varchar | 8000 | 1 |  |  |  |
| UPC | varchar | 8000 | 1 |  |  |  |
| ItemType | varchar | 8000 | 1 |  |  |  |
| KeyStory | varchar | 8000 | 1 |  |  |  |
| RoyaltyType | varchar | 8000 | 1 |  |  |  |
| RoyaltyAmount | decimal | 9 | 1 |  |  |  |
| RoyaltyPercent | decimal | 9 | 1 |  |  |  |
| TotalFOB | float | 8 | 1 |  |  |  |
| CNDescription | varchar | 8000 | 1 |  |  |  |
| SellingStatus | varchar | 8000 | 1 |  |  |  |
| giftCardType | varchar | 8000 | 1 |  |  |  |
| AccessoryType | varchar | 8000 | 1 |  |  |  |
| LicensedCollection | varchar | 8000 | 1 |  |  |  |
| LICEN | varchar | 8000 | 1 |  |  |  |
| LICEN2 | bit | 1 | 1 |  |  |  |
| Licensor | varchar | 8000 | 1 |  |  |  |
| DepartmentSortOrder | int | 4 | 1 |  |  |  |
| PlushEyeColor | varchar | 8000 | 1 |  |  |  |
| PlushFurColor | varchar | 8000 | 1 |  |  |  |
| PlushHeight | float | 8 | 1 |  |  |  |
| PlushWeight | varchar | 8000 | 1 |  |  |  |
| WebExclusive | bit | 1 | 1 |  |  |  |
| Silhouette | varchar | 8000 | 1 |  |  |  |
| Outfits | varchar | 8000 | 1 |  |  |  |
| ItemGroupID | varchar | 8000 | 1 |  |  |  |
| Category1 | varchar | 8000 | 1 |  |  |  |
| Category2 | varchar | 8000 | 1 |  |  |  |
| ProductCategory | varchar | 8000 | 1 |  |  |  |
| FloorSet | varchar | 8000 | 1 |  |  |  |
| COO | varchar | 8000 | 1 |  |  |  |
| COO_Desc | varchar | 8000 | 1 |  |  |  |
| InDate | date | 3 | 1 |  |  |  |
| OutDate | date | 3 | 1 |  |  |  |
| WarningHangtag | varchar | 8000 | 1 |  |  |  |
| SportsTeams | varchar | 8000 | 1 |  |  |  |
| ModelGroupID | varchar | 8000 | 1 |  |  |  |
| BarcodeType | varchar | 8000 | 1 |  |  |  |
| isEndlessAisleEligible | varchar | 8000 | 1 |  |  |  |
| HTSCode | varchar | 8000 | 1 |  |  |  |
| HTSCodeDesc | varchar | 8000 | 1 |  |  |  |
| US_HTS_Code | varchar | 8000 | 1 |  |  |  |
| CAN_HTS_Code | varchar | 8000 | 1 |  |  |  |
| UK_HTS_Code | varchar | 8000 | 1 |  |  |  |
| TaxItemGroupCode | varchar | 8000 | 1 |  |  |  |
