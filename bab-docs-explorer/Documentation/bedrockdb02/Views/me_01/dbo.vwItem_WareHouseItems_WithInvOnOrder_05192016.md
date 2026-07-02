# dbo.vwItem_WareHouseItems_WithInvOnOrder_05192016

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwItem_WareHouseItems_WithInvOnOrder_05192016"]
    dbo_ib_inventory_total(["dbo.ib_inventory_total"]) --> VIEW
    dbo_ib_on_order(["dbo.ib_on_order"]) --> VIEW
    dbo_location(["dbo.location"]) --> VIEW
    dbo_size_master(["dbo.size_master"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_size(["dbo.style_size"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_inventory_total |
| dbo.ib_on_order |
| dbo.location |
| dbo.size_master |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_size |
| dbo.upc |

## View Code

```sql
CREATE VIEW [dbo].[vwItem_WareHouseItems_WithInvOnOrder_05192016]
AS 

SELECT u.upc_number, l.location_code, min(ioo.receipt_date +10) as receipt_date
from	OURSMERCHDB01.me_01.dbo.ib_on_order ioo
INNER JOIN me_01.dbo.sku sku (nolock) ON 	ioo.sku_id = sku.sku_id 
INNER JOIN me_01.dbo.upc u (nolock) ON u.sku_id = sku.sku_id 
INNER JOIN me_01.dbo.style st (nolock) ON st.style_id = sku.style_id 
INNER JOIN me_01.dbo.style_color sc (nolock) ON sc.style_color_id = sku.style_color_id 
INNER JOIN me_01.dbo.style_size sz (nolock)	ON sz.style_size_id = sku.style_size_id 
INNER JOIN me_01.dbo.size_master sm (nolock) ON sm.size_master_id = sz.size_master_id
INNER JOIN me_01.dbo.ib_inventory_total iit ON iit.sku_id = sku.sku_id
INNER JOIN me_01.dbo.location l ON iit.location_id = l.location_id

where	cast(convert(varchar, ioo.receipt_date,101)as datetime) >= cast(convert(varchar, getdate(),101)as datetime)
group by u.upc_number, l.location_code, ioo.document_number
having sum(on_order_units) > 0
```

