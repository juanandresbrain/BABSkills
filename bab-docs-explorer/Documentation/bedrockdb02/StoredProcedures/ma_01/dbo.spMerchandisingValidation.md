# dbo.spMerchandisingValidation

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingValidation"]
    dbo_product_dim(["dbo.product_dim"]) --> SP
    dbo_vwDW_WeeklyOnHand_StyleColor(["dbo.vwDW_WeeklyOnHand_StyleColor"]) --> SP
    dbo_vwDW_WeeklyOnOrder_StyleColor(["dbo.vwDW_WeeklyOnOrder_StyleColor"]) --> SP
    dbo_vwDW_WeeklySales_StyleColor(["dbo.vwDW_WeeklySales_StyleColor"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |
| dbo.vwDW_WeeklyOnHand_StyleColor |
| dbo.vwDW_WeeklyOnOrder_StyleColor |
| dbo.vwDW_WeeklySales_StyleColor |

## Stored Procedure Code

```sql
-- =============================================
```

