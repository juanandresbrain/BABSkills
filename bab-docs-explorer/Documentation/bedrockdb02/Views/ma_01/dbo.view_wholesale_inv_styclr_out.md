# dbo.view_wholesale_inv_styclr_out

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_wholesale_inv_styclr_out"]
    dbo_color(["dbo.color"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_vendor(["dbo.style_vendor"]) --> VIEW
    dbo_syn_view_wholesale_inventory_sku(["dbo.syn_view_wholesale_inventory_sku"]) --> VIEW
    dbo_vendor(["dbo.vendor"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.color |
| dbo.style |
| dbo.style_color |
| dbo.style_vendor |
| dbo.syn_view_wholesale_inventory_sku |
| dbo.vendor |

## View Code

```sql
create view dbo.view_wholesale_inv_styclr_out 

AS
SELECT
sv.style_vendor_id,
s.style_id, 
sc.style_color_id,
c.color_id,
SUM(ISNULL(wi.available_on_hand, 0)) AS available_on_hand,
SUM(ISNULL(wi.original_available_on_hand, 0)) AS original_available_on_hand
FROM style s
INNER JOIN style_vendor sv on sv.style_id = s.style_id
INNER JOIN vendor v on v.vendor_id = sv.vendor_id 
INNER JOIN style_color sc on s.style_id = sc.style_id
INNER JOIN color c ON c.color_id = sc.color_id
LEFT OUTER JOIN syn_view_wholesale_inventory_sku wi ON wi.style_code = s.style_code AND wi.color_code = c.color_code AND sc.color_id = c.color_id AND wi.vendor_id = v.vendor_id
group by sv.style_vendor_id, s.style_id, sc.style_color_id, c.color_id
```

