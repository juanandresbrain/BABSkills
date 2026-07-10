# DOMO.vwMA_WeeklyOnHand

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwMA_WeeklyOnHand"]
    dbo_vwDOMO_WeeklyOnHand_StyleColor(["dbo.vwDOMO_WeeklyOnHand_StyleColor"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDOMO_WeeklyOnHand_StyleColor |

## View Code

```sql
CREATE view [DOMO].[vwMA_WeeklyOnHand]

as

select * 
from bedrockdb02.ma_01.dbo.vwDOMO_WeeklyOnHand_StyleColor
```

