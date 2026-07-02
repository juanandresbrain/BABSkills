# dbo.DC_MOVE_POS_ADDL_INFO

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_MOVE_POS_ADDL_INFO"]
    dbo_POS_ITEM_ADDL_INFO(["dbo.POS_ITEM_ADDL_INFO"]) --> SP
    dbo_TMP_POS_ITEM_ADDL_INFO(["dbo.TMP_POS_ITEM_ADDL_INFO"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.POS_ITEM_ADDL_INFO |
| dbo.TMP_POS_ITEM_ADDL_INFO |

## Stored Procedure Code

```sql

```

