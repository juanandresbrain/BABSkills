# dbo.vwTradeArea

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwTradeArea"]
    dbo_store_dim(["dbo.store_dim"]) --> VIEW
    dbo_trade_area_dim(["dbo.trade_area_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_dim |
| dbo.trade_area_dim |

## View Code

```sql
CREATE              VIEW dbo.vwTradeArea
--WITH SCHEMABINDING    
AS

SELECT   
sd.store_id as Trade_Area_StoreID,
ta.postal_code


FROM  dbo.trade_area_dim ta  
JOIN  dbo.store_dim sd ON ta.store_key = sd.store_key
```

