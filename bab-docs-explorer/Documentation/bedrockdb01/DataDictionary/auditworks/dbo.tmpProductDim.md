# dbo.tmpProductDim

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 0 | YES |  |  |
| sku | bigint | 8 | 1 |  |  |  |
| activation_date | datetime | 8 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| style_desc | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 20 | 1 |  |  |  |
| color_desc | varchar | 20 | 1 |  |  |  |
| product_desc | varchar | 40 | 1 |  |  |  |
| subclass | varchar | 20 | 1 |  |  |  |
| class | varchar | 20 | 1 |  |  |  |
| department | varchar | 20 | 1 |  |  |  |
| department_code | varchar | 20 | 1 |  |  |  |
| division | varchar | 20 | 1 |  |  |  |
| chain | varchar | 20 | 1 |  |  |  |
| concept | varchar | 20 | 1 |  |  |  |
| priceline_code | varchar | 20 | 1 |  |  |  |
| subclass_code | varchar | 20 | 1 |  |  |  |
| class_code | varchar | 20 | 1 |  |  |  |
| primary_vendor_code | varchar | 20 | 1 |  |  |  |
| primary_vendor_name | varchar | 50 | 1 |  |  |  |
| alt_primary_vendor_code | varchar | 20 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| price_with_vat | decimal | 9 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| euro_value | decimal | 9 | 1 |  |  |  |
| merch_status | varchar | 6 | 1 |  |  |  |
| wss_reportable | varchar | 6 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| current_selling_retail_home | decimal | 9 | 1 |  |  |  |
| jurisdiction_code | varchar | 20 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 1 |  |  |  |
| cdn_value | decimal | 9 | 1 |  |  |  |
| INS_DT | datetime | 8 | 0 |  |  |  |
| UPDT_DT | datetime | 8 | 0 |  |  |  |
| ETL_LOG_ID | int | 4 | 0 |  |  |  |
| ETL_EVNT_ID | int | 4 | 0 |  |  |  |
| GENDER | varchar | 10 | 1 |  |  |  |
| CORE_FASH_CD | varchar | 10 | 1 |  |  |  |
| INLINE_CD | varchar | 30 | 1 |  |  |  |
| ScorecardCategory | varchar | 50 | 1 |  |  |  |
