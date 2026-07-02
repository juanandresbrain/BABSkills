# dbo.view_dl_pack_upc

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_pack_upc"]
    dbo_dl_pack_upc(["dbo.dl_pack_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_pack_upc |

## View Code

```sql
create view dbo.view_dl_pack_upc AS
SELECT dl_pack_upc_id,
   record_no,
   upc_number,
   activation_date,
   pack_code
FROM dl_pack_upc
```

