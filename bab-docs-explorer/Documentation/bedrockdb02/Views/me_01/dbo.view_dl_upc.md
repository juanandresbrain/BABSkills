# dbo.view_dl_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_upc"]
    dbo_dl_upc(["dbo.dl_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_upc |

## View Code

```sql
create view dbo.view_dl_upc AS
SELECT dl_upc_id,
   record_no,
   vendor_code,
   vendor_style,
   color_code,
   style_color_short_desc,
   style_color_long_desc,
   style_color_fashion_flag,
   style_color_reorder_flag,
   nrf_code,
   size_category_code,
   size_code,
   style_size_ticket_lbl_override,
   style_size_reorder_flag,
   upc_number,
   upc_type,
   activation_date,
   upc_first_part_length
FROM dl_upc
```

