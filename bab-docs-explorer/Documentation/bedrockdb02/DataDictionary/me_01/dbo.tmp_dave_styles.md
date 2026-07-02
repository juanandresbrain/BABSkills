# dbo.tmp_dave_styles

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_number | varchar | 14 | 1 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| style_desc | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 3 | 0 |  |  |  |
| color_desc | varchar | 8 | 0 |  |  |  |
| subclass_desc | varchar | 20 | 0 |  |  |  |
| class_desc | varchar | 20 | 0 |  |  |  |
| dept_desc | varchar | 20 | 0 |  |  |  |
| dept_code | varchar | 20 | 0 |  |  |  |
| subclass_code | varchar | 20 | 0 |  |  |  |
| div_desc | varchar | 20 | 0 |  |  |  |
| chain_desc | varchar | 20 | 0 |  |  |  |
| concept_desc | varchar | 20 | 0 |  |  |  |
| current_selling_retail_home | decimal | 9 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| primary_vendor_code | varchar | 20 | 0 |  |  |  |
| primary_vendor_name | varchar | 50 | 0 |  |  |  |
| alt_primary_vendor_code | varchar | 20 | 1 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| reorderable_flag | bit | 1 | 0 |  |  |  |
| original_retail_home | decimal | 9 | 1 |  |  |  |
| price_with_vat | decimal | 9 | 1 |  |  |  |
| current_selling_euro | decimal | 9 | 1 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| jurisdiction_code | varchar | 20 | 0 |  |  |  |

