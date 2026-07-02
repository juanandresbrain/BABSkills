# dbo.dl_style_task_bus_rule_phs_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_style_task_bus_rule_phs_$sp"]
    dbo_dl_style_task(["dbo.dl_style_task"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_task |

## Stored Procedure Code

```sql
create proc dbo.dl_style_task_bus_rule_phs_$sp (
   @dl_style_task_id bigint,
   @total_schema_rejects bigint,
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

   BEGIN TRAN  
      UPDATE dl_style_task
      SET current_phase = 3, 
         total_schema_rejects = @total_schema_rejects,
         max_dl_style_id = @max_dl_style_id,
         max_dl_style_retail_id = @max_dl_style_retail_id,
         max_dl_style_vendor_id = @max_dl_style_vendor_id,
         max_dl_style_attribute_set_id = @max_dl_style_attr_set_id,
         max_dl_style_custom_prop_id = @max_dl_style_custom_prop_id,
         max_dl_style_attachment_id = @max_dl_style_attachment_id,
         max_dl_style_description_id = @max_dl_style_description_id,
         max_dl_upc_id = @max_dl_upc_id,
         max_dl_pack_upc_id = @max_dl_pack_upc_id,
         max_dl_style_color_retail_id = @max_dl_style_color_retail_id,
         max_dl_style_pricing_group_id = @max_dl_style_pricing_grp_id,
         max_dl_style_prc_grp_color_id = @max_dl_style_prc_grp_clr_id,
         max_dl_style_location_id = @max_dl_style_location_id,
         max_dl_style_location_color_id = @max_dl_style_loc_color_id,
         max_dl_style_color_desc_id = @max_dl_style_color_desc_id,
         max_dl_style_size_desc_id = @max_dl_style_size_desc_id
      WHERE dl_style_task_id = @dl_style_task_id
   COMMIT  
END
```

