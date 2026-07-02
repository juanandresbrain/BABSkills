# dbo.Sl_Sv_NextID

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Sv_NextID"]
    dbo_Sv_NextID(["dbo.Sv_NextID"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sv_NextID |

## View Code

```sql
create view  [dbo].[Sl_Sv_NextID] 
(table_id, table_name, next_id, max_id)
AS SELECT table_id, table_name, next_id, max_id
FROM fn_01.dbo.Sv_NextID
```

