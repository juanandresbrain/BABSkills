# dbo.update_phys_inv_table_$sp_091609

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.update_phys_inv_table_$sp_091609"]
    dbo_color(["dbo.color"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_inventory_control(["dbo.inventory_control"]) --> SP
    dbo_keith_view_inventory_units(["dbo.keith_view_inventory_units"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_physical_inventory(["dbo.physical_inventory"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_color(["dbo.style_color"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
    dbo_upc(["dbo.upc"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.color |
| dbo.hierarchy_group |
| dbo.inventory_control |
| dbo.keith_view_inventory_units |
| dbo.location |
| dbo.physical_inventory |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_group |
| dbo.upc |

## Stored Procedure Code

```sql
create  PROCEDURE [dbo].[update_phys_inv_table_$sp] (@sp  DECIMAL(12,0))

AS
BEGIN

declare @DocId as DECIMAL(12,0)
set @DocId = @sp

DELETE FROM physical_inventory
WHERE inventory_control_no = 
(
	SELECT document_no
	FROM inventory_control
	WHERE inventory_control_id = @DocId
)

INSERT INTO 
	physical_inventory (inventory_control_no, location_code, style_code, color_code, hierarchy_group_code, hierarchy_group_short_label, counted_quantity, counted_cost, transaction_units, transaction_cost, short_desc, delta_units, delta_cost)
SELECT 
	ic.document_no AS inventory_control_no, 
	l.location_code AS location_code, 
	s.style_code AS 	style_code, 
	c.color_code AS color_code, 
	hg.hierarchy_group_code AS hierarchy_group_code, 
	--u.upc_number AS upc_number, 
	hg.hierarchy_group_short_label AS hierarchy_group_short_label, 
	ISNULL(viu.counted_units, 0) AS counted_quantity, 
	ISNULL(viu.counted_cost, 0) AS counted_cost, 
	ISNULL(viu.book_qty, 0) AS transaction_units, 
	ISNULL(viu.cost, 0) AS transaction_cost, 
	s.short_desc AS short_desc, 
	ISNULL(viu.shrink_units, 0) AS delta_units, 
	ISNULL(viu.shrink_cost, 0) AS delta_cost
FROM 
	inventory_control ic, 
	location l, 
	style s, 
	color c, 
	sku k, 
	style_color sc, 
	hierarchy_group hg, 
	style_group sg, 
	keith_view_inventory_units viu/*, 
	(
		SELECT 
			sku_id, 
			MIN(upc_number) AS upc_number 
		FROM 
			upc 
		GROUP BY 
			sku_id
	) AS u*/
WHERE 
	ic.inventory_control_id = viu.inventory_control_id
	AND l.location_id = viu.location_id
	AND k.sku_id = viu.sku_id
	AND k.style_color_id = sc.style_color_id
	AND sc.color_id = c.color_id
	AND s.style_id = sc.style_id
	--AND u.sku_id = viu.sku_id 
	AND sg.style_id = s.style_id 
	AND sg.hierarchy_group_id = hg.hierarchy_group_id
	AND ic.inventory_control_id = @DocId

UPDATE
	physical_inventory
SET upc_number = 
(
	SELECT 
		MIN(upc_number)
	FROM
		upc, sku, style_color, style, color
	WHERE upc.sku_id = sku.sku_id
	AND sku.style_color_id = style_color.style_color_id
	AND style_color.style_id = style.style_id
	AND style_color.color_id = color.color_id
	AND physical_inventory.style_code = style.style_code
	AND physical_inventory.color_code = color.color_code
)

END
```

