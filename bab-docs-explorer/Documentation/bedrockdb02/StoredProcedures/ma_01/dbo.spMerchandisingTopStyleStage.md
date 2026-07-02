# dbo.spMerchandisingTopStyleStage

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingTopStyleStage"]
    dbo_rptCurrRetail(["dbo.rptCurrRetail"]) --> SP
    dbo_rptDoorCount(["dbo.rptDoorCount"]) --> SP
    dbo_rptInventory(["dbo.rptInventory"]) --> SP
    dbo_rptTopStyleTY(["dbo.rptTopStyleTY"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_vwDW_AgedStyles(["dbo.vwDW_AgedStyles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.rptCurrRetail |
| dbo.rptDoorCount |
| dbo.rptInventory |
| dbo.rptTopStyleTY |
| dbo.style |
| dbo.vwDW_AgedStyles |

## Stored Procedure Code

```sql

```

