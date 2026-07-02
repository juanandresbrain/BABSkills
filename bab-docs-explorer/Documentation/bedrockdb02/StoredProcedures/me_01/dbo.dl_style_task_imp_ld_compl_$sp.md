# dbo.dl_style_task_imp_ld_compl_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_style_task_imp_ld_compl_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
create proc [dbo].[dl_style_task_imp_ld_compl_$sp] (
   @max_dl_style_id bigint,
   @max_dl_style_retail_id bigint,
   @max_dl_style_vendor_id bigint,
   @max_dl_style_attr_set_id bigint,
   @max_dl_style_custom_prop_id bigint,
   @max_dl_style_attachment_id bigint,
   @max_dl_style_description_id bigint,
   @max_dl_upc_id bigint,
   @max_dl_pack_upc_id bigint,
   @max_dl_style_color_retail_id bigint,
   @max_dl_style_pricing_grp_id bigint,
   @max_dl_style_prc_grp_clr_id bigint,
   @max_dl_style_location_id bigint,
   @max_dl_style_loc_color_id bigint,
   @max_dl_style_color_desc_id bigint,
   @max_dl_style_size_desc_id bigint
)

AS

BEGIN
   SET XACT_ABORT ON
   SET IMPLICIT_TRANSACTIONS OFF

   IF @max_dl_style_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style') AND name = N'dl_style_$ndx1')
            BEGIN
               CREATE INDEX dl_style_$ndx1 ON dl_style (style_code) WITH PAD_INDEX, FILLFACTOR=100
            END
            
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style') AND name = N'dl_style_$ndx2')
            BEGIN
               CREATE INDEX dl_style_$ndx2 ON dl_style (vendor_code, vendor_style) WITH PAD_INDEX, FILLFACTOR=100
            END            
            
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style') AND name = N'dl_style_$ndx3')
            BEGIN
               CREATE INDEX dl_style_$ndx3 ON dl_style (style_code, vendor_code) WITH PAD_INDEX, FILLFACTOR=100
            END            
         
         UPDATE STATISTICS dl_style
      END
      
   IF @max_dl_style_retail_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_retail') AND name = N'dl_style_retail_$ndx1')
            BEGIN
               CREATE INDEX dl_style_retail_$ndx1 ON dl_style_retail (style_code, jurisdiction_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_retail
      END
      
   IF @max_dl_style_vendor_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_vendor') AND name = N'dl_style_vendor_$ndx1')
            BEGIN
               CREATE INDEX dl_style_vendor_$ndx1 ON dl_style_vendor (style_code, vendor_code) WITH PAD_INDEX, FILLFACTOR=100
            END
            
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_vendor') AND name = N'dl_style_vendor_$ndx2')
            BEGIN
               CREATE INDEX dl_style_vendor_$ndx2 ON dl_style_vendor (vendor_code, vendor_style) WITH PAD_INDEX, FILLFACTOR=100
            END            
         
         UPDATE STATISTICS dl_style_vendor
      END
      
   IF @max_dl_style_attr_set_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_attribute_set') AND name = N'dl_style_attribute_set_$ndx1')
            BEGIN
               CREATE INDEX dl_style_attribute_set_$ndx1 ON dl_style_attribute_set (action_type, style_code, attribute_code, attribute_set_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_attribute_set
      END
      
   IF @max_dl_style_custom_prop_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_custom_property') AND name = N'dl_style_custom_property_$ndx1')
            BEGIN
               CREATE INDEX dl_style_custom_property_$ndx1 ON dl_style_custom_property (style_code, cust_prop_code, custom_property_value) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_custom_property
      END
      
   IF @max_dl_style_attachment_id <> 0
      BEGIN
         UPDATE STATISTICS dl_style_attachment
      END
      
   IF @max_dl_style_description_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_description') AND name = N'dl_style_description_$ndx1')
            BEGIN
               CREATE INDEX dl_style_description_$ndx1 ON dl_style_description (style_code, locale_identifier) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_description
      END
      
   IF @max_dl_upc_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_upc') AND name = N'dl_upc_$ndx1')
            BEGIN
               CREATE INDEX dl_upc_$ndx1 ON dl_upc (upc_number) WITH PAD_INDEX, FILLFACTOR=100
            END
            
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_upc') AND name = N'dl_upc_$ndx2')
            BEGIN
               CREATE INDEX dl_upc_$ndx2 ON dl_upc (vendor_code, vendor_style, color_code) WITH PAD_INDEX, FILLFACTOR=100
            END
            
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_upc') AND name = N'dl_upc_$ndx3')
            BEGIN
               CREATE INDEX dl_upc_$ndx3 ON dl_upc (vendor_code, vendor_style) WITH PAD_INDEX, FILLFACTOR=100
            END            
         
         UPDATE STATISTICS dl_upc
      END
      
   IF @max_dl_pack_upc_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_pack_upc') AND name = N'dl_pack_upc_$ndx1')
            BEGIN
               CREATE INDEX dl_pack_upc_$ndx1 ON dl_pack_upc (upc_number) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_pack_upc
      END
      
   IF @max_dl_style_color_retail_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_color_retail') AND name = N'dl_style_color_retail_$ndx1')
            BEGIN
               CREATE INDEX dl_style_color_retail_$ndx1 ON dl_style_color_retail (style_code, color_code, jurisdiction_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_color_retail
      END
      
   IF @max_dl_style_pricing_grp_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_pricing_group') AND name = N'dl_style_pricing_group_$ndx1')
            BEGIN
               CREATE INDEX dl_style_pricing_group_$ndx1 ON dl_style_pricing_group (style_code, pricing_group_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_pricing_group
      END
      
   IF @max_dl_style_prc_grp_clr_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_pricing_grp_clr') AND name = N'dl_style_pricing_grp_clr_$ndx1')
            BEGIN
               CREATE INDEX dl_style_pricing_grp_clr_$ndx1 ON dl_style_pricing_grp_clr (style_code, pricing_group_code, color_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_pricing_grp_clr
      END
      
   IF @max_dl_style_location_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_location') AND name = N'dl_style_location_$ndx1')
            BEGIN
               CREATE INDEX dl_style_location_$ndx1 ON dl_style_location (style_code, location_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_location
      END
      
   IF @max_dl_style_loc_color_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_location_color') AND name = N'dl_style_location_color_$ndx1')
            BEGIN
               CREATE INDEX dl_style_location_color_$ndx1 ON dl_style_location_color (style_code, location_code, color_code) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_location_color
      END
      
   IF @max_dl_style_color_desc_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_color_desc') AND name = N'dl_style_color_desc_$ndx1')
            BEGIN
               CREATE INDEX dl_style_color_desc_$ndx1 ON dl_style_color_desc (style_code, color_code, locale_identifier) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_color_desc
      END
      
   IF @max_dl_style_size_desc_id <> 0
      BEGIN
         IF NOT EXISTS (SELECT * FROM sysindexes WHERE id = OBJECT_ID(N'dl_style_size_desc') AND name = N'dl_style_size_desc_$ndx1')
            BEGIN
               CREATE INDEX dl_style_size_desc_$ndx1 ON dl_style_size_desc (style_code, size_code, locale_identifier) WITH PAD_INDEX, FILLFACTOR=100
            END
         
         UPDATE STATISTICS dl_style_size_desc
      END
END
```

