# Azure.vwPOSOutbound_WebReturns

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_WebReturns"]
    dbo_tmpWebSalesForPOSReturns(["dbo.tmpWebSalesForPOSReturns"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpWebSalesForPOSReturns |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_WebReturns] AS

select * 
from [Bearcluster01.SQL.Buildabear.com].WebOrderProcessing.dbo.tmpWebSalesForPOSReturns
```

