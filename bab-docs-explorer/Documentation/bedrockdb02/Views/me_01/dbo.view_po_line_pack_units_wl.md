# dbo.view_po_line_pack_units_wl

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_po_line_pack_units_wl"]
    dbo_po_detail(["dbo.po_detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.po_detail |

## View Code

```sql
create view dbo.view_po_line_pack_units_wl 
AS
SELECT po_id, po_line_id, sum(ordered_units) AS total_pack_units
FROM po_detail d
WHERE d.pack_id IS NOT NULL 
GROUP BY po_id, po_line_id
```

