# dbo.product_dim_wip

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 1 |  |  |  |
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
| reorder_flag | bit | 1 | 1 |  |  |  |
| euro_value | decimal | 9 | 1 |  |  |  |
| merch_status | varchar | 8000 | 1 |  |  |  |
| wss_reportable | varchar | 8000 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| color_id | int | 4 | 1 |  |  |  |
| current_selling_retail_home | decimal | 9 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
