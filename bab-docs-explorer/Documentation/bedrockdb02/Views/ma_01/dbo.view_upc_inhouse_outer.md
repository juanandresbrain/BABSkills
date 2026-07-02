# dbo.view_upc_inhouse_outer

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_upc_inhouse_outer"]
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
create view dbo.view_upc_inhouse_outer AS
select s.sku_id,u.upc_number from upc u RIGHT JOIN sku s
on 
u.sku_id = s.sku_id  AND  u.upc_type = 2
```

