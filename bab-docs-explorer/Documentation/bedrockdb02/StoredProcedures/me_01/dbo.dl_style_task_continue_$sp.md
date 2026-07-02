# dbo.dl_style_task_continue_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_style_task_continue_$sp"]
    dbo_dl_style_task(["dbo.dl_style_task"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_style_task |

## Stored Procedure Code

```sql
create proc [dbo].[dl_style_task_continue_$sp] 
(
   @dl_style_task_id bigint OUTPUT,
   @start_date smalldatetime OUTPUT,
   @current_phase tinyint OUTPUT,   
   @action_type tinyint OUTPUT,
   @file_name nvarchar(255) OUTPUT,
   @encoding tinyint OUTPUT,
   @max_rejects bigint OUTPUT,
   @temp_folder nvarchar(255) OUTPUT,
   @threads int OUTPUT,
   @max_rows_per_batch int OUTPUT,  
   @pct_rows_per_batch float OUTPUT,
   @total_schema_rejects bigint OUTPUT,
   @tot_dl_style_br_rej bigint OUTPUT,
   @tot_dl_style_retail_br_rej bigint OUTPUT,
   @tot_dl_style_vendor_br_rej bigint OUTPUT,
   @tot_dl_style_attr_set_br_rej bigint OUTPUT,
   @tot_dl_style_cust_prp_br_rej bigint OUTPUT,
   @tot_dl_style_attach_br_rej bigint OUTPUT,
   @tot_dl_style_desc_br_rej bigint OUTPUT,
   @tot_dl_upc_br_rej bigint OUTPUT,
   @tot_dl_pack_upc_br_rej bigint OUTPUT,
   @tot_dl_style_clr_ret_br_rej bigint OUTPUT,
   @tot_dl_style_prc_grp_br_rej bigint OUTPUT,
   @tot_dl_st_prc_grp_clr_br_rej bigint OUTPUT,
   @tot_dl_style_location_br_rej bigint OUTPUT,
   @tot_dl_style_loc_clr_br_rej bigint OUTPUT,
   @tot_dl_style_clr_desc_br_rej bigint OUTPUT,
   @tot_dl_style_sz_desc_br_rej bigint OUTPUT   
)

AS

DECLARE
   
   @failure int,
   @in_progress_flag bit

BEGIN
   SET XACT_ABORT ON
   SET IMPLICIT_TRANSACTIONS OFF

   SET @failure = 1  
      
   SELECT @dl_style_task_id = ISNULL(MAX(dl_style_task_id), -1) 
   FROM dl_style_task

   IF @dl_style_task_id <> -1
      BEGIN    
         SELECT @in_progress_flag = in_progress_flag,
            @start_date = start_date,
            @current_phase = current_phase,  
            @action_type = action_type,
            @file_name = file_name,
            @encoding = encoding,
            @max_rejects = max_rejects,
            @temp_folder = temp_folder,
            @threads = threads,
            @max_rows_per_batch = max_rows_per_batch,  
            @pct_rows_per_batch = pct_rows_per_batch,
            @total_schema_rejects = total_schema_rejects,
            @tot_dl_style_br_rej = tot_dl_style_br_rej,
            @tot_dl_style_retail_br_rej = tot_dl_style_retail_br_rej,
            @tot_dl_style_vendor_br_rej = tot_dl_style_vendor_br_rej,
            @tot_dl_style_attr_set_br_rej = tot_dl_style_attr_set_br_rej,
            @tot_dl_style_cust_prp_br_rej = tot_dl_style_cust_prop_br_rej,
            @tot_dl_style_attach_br_rej = tot_dl_style_attach_br_rej,
            @tot_dl_style_desc_br_rej = tot_dl_style_desc_br_rej,
            @tot_dl_upc_br_rej = tot_dl_upc_br_rej,
            @tot_dl_pack_upc_br_rej = tot_dl_pack_upc_br_rej,
            @tot_dl_style_clr_ret_br_rej = tot_dl_style_color_ret_br_rej,
            @tot_dl_style_prc_grp_br_rej = tot_dl_style_prc_grp_br_rej,
            @tot_dl_st_prc_grp_clr_br_rej = tot_dl_stl_prc_grp_clr_br_rej,
            @tot_dl_style_location_br_rej = tot_dl_style_location_br_rej,
            @tot_dl_style_loc_clr_br_rej = tot_dl_style_loc_color_br_rej,
            @tot_dl_style_clr_desc_br_rej = tot_dl_style_color_desc_br_rej,
            @tot_dl_style_sz_desc_br_rej = tot_dl_style_size_desc_br_rej         
         FROM dl_style_task 
         WHERE dl_style_task_id = @dl_style_task_id
         
         IF @in_progress_flag <> 0
            BEGIN
               SET @failure = 0
            END         
      END
  
  RETURN @failure
END
```

