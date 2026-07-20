# dbo.product_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | varchar | 8000 | 1 |  |  |  |
| sku | bigint | 8 | 1 |  |  |  |
| activation_date | datetime2 | 8 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| style_desc | varchar | 8000 | 1 |  |  |  |
| MerchStyle | varchar | 8000 | 1 |  |  |  |
| Style | varchar | 8000 | 1 |  |  |  |
| color_code | varchar | 8000 | 1 |  |  |  |
| color_desc | varchar | 8000 | 1 |  |  |  |
| product_desc | varchar | 8000 | 1 |  |  |  |
| Product | varchar | 8000 | 1 |  |  |  |
| subclass | varchar | 8000 | 1 |  |  |  |
| MerchSubclass | varchar | 8000 | 1 |  |  |  |
| class | varchar | 8000 | 1 |  |  |  |
| MerchClass | varchar | 8000 | 1 |  |  |  |
| department | varchar | 8000 | 1 |  |  |  |
| department_code | varchar | 8000 | 1 |  |  |  |
| division | varchar | 8000 | 1 |  |  |  |
| chain | varchar | 8000 | 1 |  |  |  |
| concept | varchar | 8000 | 1 |  |  |  |
| priceline_code | varchar | 8000 | 1 |  |  |  |
| subclass_code | varchar | 8000 | 1 |  |  |  |
| class_code | varchar | 8000 | 1 |  |  |  |
| ClassCodeKey | varchar | 8000 | 1 |  |  |  |
| DivisionCodeKey | varchar | 8000 | 1 |  |  |  |
| StyleCodeKey | varchar | 8000 | 1 |  |  |  |
| primary_vendor_code | varchar | 8000 | 1 |  |  |  |
| primary_vendor_name | varchar | 8000 | 1 |  |  |  |
| alt_primary_vendor_code | varchar | 8000 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| price_with_vat | decimal | 9 | 1 |  |  |  |
| euro_value | decimal | 9 | 1 |  |  |  |
| merch_status | varchar | 8000 | 1 |  |  |  |
| wss_reportable | varchar | 8000 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| USDollarCurrentRetail | decimal | 9 | 1 |  |  |  |
| CADollarCurrentRetail | decimal | 9 | 1 |  |  |  |
| JurisdictionCodeKey | varchar | 8000 | 1 |  |  |  |
| Jurisdiction | varchar | 8000 | 1 |  |  |  |
| MerchClassCodeKey | varchar | 8000 | 1 |  |  |  |
| MerchSubclassCodeKey | varchar | 8000 | 1 |  |  |  |
| MerchStyleCodeKey | varchar | 8000 | 1 |  |  |  |
| plain_Jurisdiction | varchar | 8000 | 1 |  |  |  |
| Exclude_From_WSS | int | 4 | 1 |  |  |  |
| Omit_From_WSS | varchar | 8000 | 1 |  |  |  |
| cmn_department_code | varchar | 8000 | 1 |  |  |  |
| cmn_department | varchar | 8000 | 1 |  |  |  |
| CommonDepartment | varchar | 8000 | 1 |  |  |  |
| cmn_class_code | varchar | 8000 | 1 |  |  |  |
| cmn_class | varchar | 8000 | 1 |  |  |  |
| CommonClass | varchar | 8000 | 1 |  |  |  |
| cmn_subclass_code | varchar | 8000 | 1 |  |  |  |
| cmn_subclass | varchar | 8000 | 1 |  |  |  |
| CommonSubclass | varchar | 8000 | 1 |  |  |  |
| cmn_style_code | varchar | 8000 | 1 |  |  |  |
| cmn_style | varchar | 8000 | 1 |  |  |  |
| CommonStyle | varchar | 8000 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| CoreFashion | varchar | 8000 | 1 |  |  |  |
| Inline | varchar | 8000 | 1 |  |  |  |
