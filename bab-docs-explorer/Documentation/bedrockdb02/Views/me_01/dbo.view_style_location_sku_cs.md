# dbo.view_style_location_sku_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_location_sku_cs"]
    dbo_style_location_sku(["dbo.style_location_sku"]) --> VIEW
    dbo_style_location_sku_cs(["dbo.style_location_sku_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.style_location_sku |
| dbo.style_location_sku_cs |

## View Code

```sql
CREATE VIEW [dbo].[view_style_location_sku_cs] 
AS
SELECT [style_location_sku_id]
      ,[style_id]
      ,[location_id]
      ,[style_color_id]
      ,[size_master_id]
	  ,[sku_id]
      ,[jurisdiction_id]
      ,[original_selling_retail]
      ,[original_valuation_retail]
      ,[original_price_status_id]
      ,[current_selling_retail]
      ,[current_valuation_retail]
      ,[current_price_status_id]
  FROM [style_location_sku]
UNION ALL
SELECT [style_location_sku_id]
      ,[style_id]
      ,[location_id]
      ,[style_color_id]
      ,[size_master_id]
	  ,[sku_id]
      ,[jurisdiction_id]
      ,[original_selling_retail]
      ,[original_valuation_retail]
      ,[original_price_status_id]
      ,[current_selling_retail]
      ,[current_valuation_retail]
      ,[current_price_status_id]
  FROM [style_location_sku_cs]
```

