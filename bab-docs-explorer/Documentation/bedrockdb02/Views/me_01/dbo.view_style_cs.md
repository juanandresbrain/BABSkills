# dbo.view_style_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_cs"]
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_cs(["dbo.style_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style |
| dbo.style_cs |

## View Code

```sql
CREATE VIEW [dbo].[view_style_cs]
AS
SELECT [style_id]
      ,[style_code]
      ,[style_type]
      ,[color_flag]
      ,[size_flag]
      ,[style_status]
      ,[active_flag]
      ,[delete_status]
      ,[long_desc]
      ,[short_desc]
      ,[season_id]
      ,[calendar_year_id]
      ,[ticket_format_id]
      ,[position_id]
      ,[size_category_id]
      ,[last_item_id]
      ,[weight]
      ,[height]
      ,[width]
      ,[depth]
      ,[plu_desc]
      ,[promo_flag]
      ,[consignment_flag]
      ,[inhouse_upc_flag]
      ,[vendor_upc_flag]
      ,[reorder_flag]
      ,[fashion_flag]
      ,[replenishable_flag]
      ,[allow_customer_back_order_flag]
      ,[create_date]
      ,[updatestamp]
      ,[last_modified]
      ,[order_multiple]
      ,[distribution_multiple]
      ,[target_selling_from_week]
      ,[target_selling_to_week]
      ,[target_selling_from_year]
      ,[target_selling_to_year]
      ,[size_grid_id]
      ,[image_path]
      ,[to_be_deleted_date]
      ,[resulting_po_predistrib_type]
      ,[document_source]
      ,[concept_code]
      ,[export_status]
      ,[allow_customer_order_flag]
      ,[threshold]
	  ,[protected_flag]
  FROM [style]
UNION ALL
SELECT [style_id]
      ,[style_code]
      ,[style_type]
      ,[color_flag]
      ,[size_flag]
      ,[style_status]
      ,[active_flag]
      ,[delete_status]
      ,[long_desc]
      ,[short_desc]
      ,[season_id]
      ,[calendar_year_id]
      ,[ticket_format_id]
      ,[position_id]
      ,[size_category_id]
      ,[last_item_id]
      ,[weight]
      ,[height]
      ,[width]
      ,[depth]
      ,[plu_desc]
      ,[promo_flag]
      ,[consignment_flag]
      ,[inhouse_upc_flag]
      ,[vendor_upc_flag]
      ,[reorder_flag]
      ,[fashion_flag]
      ,[replenishable_flag]
      ,[allow_customer_back_order_flag]
      ,[create_date]
      ,[updatestamp]
      ,[last_modified]
      ,[order_multiple]
      ,[distribution_multiple]
      ,[target_selling_from_week]
      ,[target_selling_to_week]
      ,[target_selling_from_year]
      ,[target_selling_to_year]
      ,[size_grid_id]
      ,[image_path]
      ,[to_be_deleted_date]
      ,[resulting_po_predistrib_type]
      ,[document_source]
      ,[concept_code]
      ,[export_status]
      ,[allow_customer_order_flag]
      ,[threshold]
	  ,[protected_flag]
  FROM [style_cs]
```

