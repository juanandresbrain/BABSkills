# dbo.view_sku_location

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_sku_location"]
    dbo_location(["dbo.location"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.location |
| dbo.sku |

## View Code

```sql
create view dbo.view_sku_location 
         (sku_id,
          style_id,
          location_id)
AS
   SELECT sk.sku_id,
          sk.style_id,
          l.location_id
     FROM sku sk,
          location l
```

