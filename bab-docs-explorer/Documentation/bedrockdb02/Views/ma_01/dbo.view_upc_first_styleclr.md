# dbo.view_upc_first_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_upc_first_styleclr"]
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sku |
| dbo.upc |

## View Code

```sql
create view dbo.view_upc_first_styleclr as
select  a.style_id, a.color_id, min(c.upc_number) upc_number
from sku a, upc c 
where a.sku_id =c.sku_id
group by a.style_id, a.color_id
```

