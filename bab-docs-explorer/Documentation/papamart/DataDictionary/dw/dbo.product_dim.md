# dbo.product_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| sku | bigint | 8 | 1 |  |  | Natural key:  from table oursmerchdb01.dbo.upc.upc:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| activation_date | datetime | 8 | 1 |  |  | from table oursmerchdb01.dbo.upc.activation_date:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| style_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.style.style_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| style_desc | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.style.style_desc:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| color_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.color.color_dcde:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| color_desc | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.color.color_short_description:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| product_desc | varchar | 40 | 1 |  |  | from table oursmerchdb01.dbo.style.short_desc + color.color_short_description:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| subclass | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| class | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| department | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| department_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| division | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| chain | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| concept | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hierarchy_group.hierarchy_group_short_label:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| priceline_code | varchar | 20 | 1 |  |  | (derived column in SSIS package) |
| subclass_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hgsub.hierarchy_group_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| class_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.hgsub.hierarchy_group_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| primary_vendor_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.vendor.vendor_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| primary_vendor_name | varchar | 50 | 1 |  |  | from table oursmerchdb01.dbo.vendor.vendor_name:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| alt_primary_vendor_code | varchar | 20 | 1 |  |  | from table oursmerchdb01.dbo.vendor.alternate_vendor_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| current_retail | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style_retail.current_selling_retail - based on hierarchy_group.group_code:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| original_retail | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style_retail.original_selling_retail:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| price_with_vat | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style_retail.current_selling_retail:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| reorder_flag | bit | 1 | 1 |  |  | from table oursmerchdb01.dbo.style.reorder_flag:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| euro_value | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style_retail.current_selling_retail:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| merch_status | varchar | 6 | 1 |  |  | CAST(merch.attribute_set_code AS VARCHAR(6)) AS merch_status, -- lookup in SSIS package |
| wss_reportable | varchar | 6 | 1 |  |  | CAST(wss.attribute_set_code AS VARCHAR(6)) AS wss_reportable,-- lookup in SSIS package |
| style_id | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style.style_id:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| color_id | smallint | 2 | 1 |  |  | from table oursmerchdb01.dbo.color.color_id:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| current_selling_retail_home | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.style_retail.current_selling_retail:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| jurisdiction_code | varchar | 20 | 1 |  |  | hardcoded based on style_code |
| jurisdiction_id | int | 4 | 1 |  |  | hardcoded based on style_code |
| cdn_value | decimal | 9 | 1 |  |  | from table oursmerchdb01.dbo.stlye_retail.current_selling_retail:  from view oursmerchdb01.dbo.vwDW_PRODUCT_Dim |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| GENDER | varchar | 10 | 1 |  |  |  |
| CORE_FASH_CD | varchar | 10 | 1 |  |  |  |
| INLINE_CD | varchar | 30 | 1 |  |  |  |
| ScorecardCategory | varchar | 50 | 1 |  |  |  |
