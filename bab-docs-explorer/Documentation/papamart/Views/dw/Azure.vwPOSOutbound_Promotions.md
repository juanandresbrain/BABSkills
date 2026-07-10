# Azure.vwPOSOutbound_Promotions

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_Promotions"]
    dbo_vwPOSOutbound_Promotions(["dbo.vwPOSOutbound_Promotions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwPOSOutbound_Promotions |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_Promotions] AS

select * from bedrockdb02.me_01.dbo.vwPOSOutbound_Promotions
```

