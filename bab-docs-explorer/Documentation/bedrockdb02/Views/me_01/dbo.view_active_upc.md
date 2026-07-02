# dbo.view_active_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_active_upc"]
    dbo_upc(["dbo.upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.upc |

## View Code

```sql
create view dbo.view_active_upc AS
SELECT     b.sku_id,
           b.max_date              AS last_activity_date,
           b.min_upc_type          AS upc_type,
           MAX(dbo.upc.upc_number) AS upc_number
FROM   dbo.upc INNER JOIN
                    (SELECT      a.sku_id,
                                 a.max_date,
                                 MIN(upc_type) min_upc_type,
                                 MAX(upc.activation_date) max_activation
                       FROM  dbo.upc,
                              (SELECT      upc.sku_id,
                                           MAX(upc.last_activity_date) max_date
                                 FROM  dbo.upc
                                GROUP BY   sku_id)   a
                      WHERE    upc.sku_id = a.sku_id
                        AND    upc.last_activity_date = a.max_date
                      GROUP BY a.sku_id, a.max_date) b
            ON  dbo.upc.sku_id = b.sku_id
           AND  dbo.upc.last_activity_date = b.max_date
           AND  dbo.upc.upc_type = b.min_upc_type
           AND (dbo.upc.activation_date = b.max_activation or b.max_activation is null)
GROUP BY b.sku_id, b.max_date, b.min_upc_type
```

